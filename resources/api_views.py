from database.models import Tech, Course
from flask import request, Response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity


class CoursesAPI(Resource): 
    @jwt_required
    def get(self):
        courses = Course.objects().to_json()
        return Response(courses, mimetype="application/json", status=200)

    # @jwt_required
    # def post(self):
    #     user_id = get_jwt_identity()
    #     body = request.get_json()
    #     movie = Movie(**body)
    #     movie.save()
    #     # user.update(push__movies=movie)
    #     # user.save()
    #     movie_id = movie.id
    #     return {'id': str(movie_id)}, 200


class TechsAPI(Resource):

    # @jwt_required
    # def put(self, id):
    #     # user_id = get_jwt_identity()
    #     movie = Movie.objects.get(id=id)
    #     body = request.get_json()
    #     movie.update(**body)
    #     return '', 200

    # @jwt_required
    # def delete(self, id):
    #     # user_id = get_jwt_identity()
    #     movie = Movie.objects.get(id=id)
    #     movie.delete()
    #     return '', 200

    @jwt_required
    def get(self):
        techs = Tech.objects.to_json()
        return Response(movies, mimetype="application/json", status=200)
