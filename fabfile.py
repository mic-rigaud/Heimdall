# @Author: michael
# @Date:   22-Feb-2018
# @Project: Blueberry
# @Last modified by:   michael
# @Last modified time: 08-Apr-2018
# @License: GNU GPL v3

import configparser
import logging
import os
import subprocess
import sys
import time
from collections import namedtuple

from application.application import application_main
from application.src.api.api_bdd import *
from application.src.api.api_rest import ApiRootContainer
from fabric.api import *
from web_server.app_factory import create_app

endpoint = namedtuple('endpoint', ['container', 'path'])

sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.getcwd())

logging.basicConfig(
    filename='./logs/blueberry.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')


def test():
    # TODO: Faire les tests et le plan de Test
    local("nosetests tests")


@task
def commit():
    local("git add -p && git commit")


def push():
    local("git push")


@task
def prepare_deploy():
    test()
    commit()
    push()


@task
def clean():
    local("rm logs/blueberry.log")


@task(alias="stapp")
def start_app(args=""):
    application_main()


@task(alias="stw")
def start_web(args=""):
    app = create_app()
    api_path = '/api-v0.0'
    endpoint_list = [
        endpoint(container=ApiRootContainer, path='/'),
    ]
    for endpt in endpoint_list:
        blueprint = endpt.container(endpt.path).blueprint
        app.register_blueprint(blueprint, url_prefix=api_path + endpt.path)
    # TODO: rendre le choix du port et ip configurable
    # TODO: Attention les logs sont envoyes dans /logs... et il y en a bcp
    app.run('localhost', 36000, debug=False)


# TODO: Faire des logs propre
@task
def install():
    config = configparser.ConfigParser()
    FNULL = open(os.devnull, 'w')
    try:
        config.read('./config/config.ini')
        if not config:
            print('No config file found!')
            exit
    except:
        print("=== Erreur lors de la lecture du fichier de configuration ===")
    # TODO: Il faut verif les param dans config.ini
    try:
        db.connect
        db.create_tables([Ip, Parametre])
        for sec in config:
            for element in config[sec]:
                print("= Ajout dans la table parametre de l element: " + sec +
                      ", " + element + ",  " + config[sec][element])
                param = Parametre.create(
                    section=sec, key=element,
                    value=config[sec][element]).save()
    except:
        print("=== La base SQL existe déjà ===")
    try:
        subprocess.check_call(["mkdir", "logs"], stderr=FNULL)
        print("= Creation du dossier logs")
    except:
        print("=== Le dossier logs existe déjà ===")
