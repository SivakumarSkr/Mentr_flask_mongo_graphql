from flask import Flask, request, Response
from database.db import initialize_db
from flask_bcrypt import Bcrypt
from resources.routes import initialize_routes
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_graphql import GraphQLView
from resources.schema import schema


app = Flask(__name__)
app.config.from_envvar("ENV_FILE_LOCATION")
api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/mentr',
    'alias': 'default',
}
initialize_db(app)
initialize_routes(api)
app.add_url_rule(
    '/graphql', view_func=GraphQLView.as_view(
        'graphql', 
        schema=schema, 
        graphql=True
        ))
app.run()
