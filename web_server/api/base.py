from flask import Blueprint
from flask_restful import Api, Resource


class ApiBaseResource(Resource):

    methods = []

    def get(self):
        return self.GET()

    def GET(self):
        return 'Not implemented'

    def post(self):
        return self.POST()

    def POST(self):
        return 'Not implemented'

class BluePrintContainer:

    routes = []

    def __init__(self, name):
        self.blueprint = self.make(name)

    def make(self, name):
        blueprint = Blueprint(name, __name__)
        api = Api(blueprint)

        for route in self.routes:
            api.add_resource(route[0], route[1])

        return blueprint
