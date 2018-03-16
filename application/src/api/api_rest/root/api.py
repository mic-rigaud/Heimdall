# @Author: michael
# @Date:   16-Feb-2018
# @Project: Blueberry
# @Filename: api.py
# @Last modified by:   michael
# @Last modified time: 16-Mar-2018
# @License: GNU GPL v3

from application.src.api.api_bdd import *
from application.src.api.api_rest.base import (ApiBaseResource,
                                               BluePrintContainer)


class ApiRoot(ApiBaseResource):
    def GET(self):
        return 'A simple api made for you :)'


class ApiIp(ApiBaseResource):
    def GET(self):
        json_return = []
        for element in Ip.select():
            json_return = json_return + [{
                "ip":
                element.ip,
                "mac":
                element.mac,
                "time_first":
                element.time_first.strftime("%Y-%m-%d %H:%M:%S"),
                "time_last":
                element.time_last.strftime("%Y-%m-%d %H:%M:%S"),
                "confiance":
                element.confiance,
                "status":
                element.status
            }]
        return json_return


class ApiParametre(ApiBaseResource):
    def GET(self):
        json_return = []
        for element in Parametre.select():
            json_return = json_return + [{
                "section": element.section,
                "key": element.key,
                "value": element.value,
            }]
        return json_return


class ApiRootContainer(BluePrintContainer):
    routes = [(ApiRoot, '/'), (ApiIp, 'ip'), (ApiParametre, 'settings')]
