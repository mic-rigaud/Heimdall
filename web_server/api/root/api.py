from api.base import ApiBaseResource, BluePrintContainer


class ApiRoot(ApiBaseResource):

    def GET(self):
        return 'A simple api made for you :)'

class ApiTest(ApiBaseResource):
    def GET(self):
        return 'Blabla Test'


class ApiRootContainer(BluePrintContainer):
    routes = [
        (ApiRoot, '/'),
        (ApiTest, '/test'),
    ]
