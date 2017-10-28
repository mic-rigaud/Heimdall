# Core
from flask import Flask, render_template


def create_app():

    app = Flask(__name__, template_folder="spa", static_folder='spa')

    @app.route('/')
    def PoloWatchSpa():
        return render_template('index.html')

    return app
