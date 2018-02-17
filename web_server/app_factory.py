import os, sys
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.getcwd())

# Support
from collections import namedtuple
endpoint = namedtuple('endpoint', ['container', 'path'])

# Core
from flask import Flask, render_template

# Container
from api import ApiRootContainer
#from api import ApiTestContainer


def create_app():

    app = Flask(__name__, template_folder="spa", static_folder='spa')

    # REST-API
    api_path = '/api-v0.0'

    endpoint_list = [
        endpoint(container=ApiRootContainer, path='/'),
    ]

    for endpt in endpoint_list:
        blueprint = endpt.container(endpt.path).blueprint
        app.register_blueprint(blueprint, url_prefix=api_path+endpt.path)


    # Serving angular app
    @app.route('/')
    def PoloWatchSpa():
        return render_template('index.html')

    return app
