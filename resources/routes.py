from .api_views import CoursesAPI, TechsAPI
from .auth import SignupAPI, LoginApi


def initialize_routes(api):
    api.add_resource(CoursesAPI, '/api/movies/<id>')
    api.add_resource(TechsAPI, '/api/movies')
    api.add_resource(SignupAPI, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
