# @Author: michael
# @Date:   26-Feb-2018
# @Project: Blueberry
# @Filename: app_factory.py
# @Last modified by:   michael
# @Last modified time: 04-Mar-2018
# @License: GNU GPL v3


import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.getcwd())

# Core
from flask import Flask, render_template

def create_app():

    app = Flask(__name__, template_folder="spa", static_folder='spa')

    # Serving angular app
    @app.route('/')
    def PoloWatchSpa():
        return render_template('index.html')

    return app
