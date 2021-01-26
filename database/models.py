from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash


class Tech(db.Document):
    name = db.StringField(required=True, unique=True)
    tech_type = db.ListField(db.StringField(max_length=100), required=True)


class Course(db.Document):
    name = db.StringField(required=True, unique=True)
    mentor = db.ReferenceField('Mentor', required=True, )
    techs = db.ListField(db.ReferenceField(Tech))
    duration = db.DecimalField(min_value=1, precision=1)
    topics = db.ListField(db.ReferenceField('Topic'))


class Topic(db.Document):
    name = db.StringField()
    course = db.LazyReferenceField(Course, reverse_delete_rule=2)


class User(db.Document):
    username = db.StringField(required=True, max_length=8, min_length=20, regex=r"^[a-zA-Z0-9_.-]+$")
    first_name = db.StringField(required=True)
    last_name = db.StringField()
    dob = db.DateTimeField(required=True)
    is_active = db.BooleanField(default=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=8)

    meta = {'allow_inheritance': True}

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)


class Mentor(User):
    skills = db.ListField(Tech, required=True)
    qualification = db.StringField(required=True)
    verfied = db.BooleanField(default=False)
    bio = db.StringField(required=True, max_length=1000)
    students = db.ListField(db.ReferenceField('Mentee'))


class Mentee(User):
    interests = db.ListField(Tech, required=False)
    current_mentor = db.ReferenceField(Mentor)    

