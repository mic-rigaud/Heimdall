#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Blueberry
  auteurs: michael
  version: 0.1
  date: 23/10/2017
'''

import logging
import configparser
import time

logging.basicConfig(filename='./log/blueberry.log',
                    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

from src.api.api_mvc import NetworkElementsDatabase
from src.api.api_telegram import ApiTelegram
from src.scans.ping_scan import PingScan

config = configparser.ConfigParser()
config.read('./config/config.ini')
if not config:
    logging.error('No config file found!')
    exit


if __name__=="__main__":
    logging.info("Initialisation de Blueberry")
    database = NetworkElementsDatabase()
    try:
        while 1:
            logging.info("Demarrage d'un {} scan".format(config.get("scan", "type")))
            net = PingScan(database, config)
            net.start()
            time.sleep(int(config.get("scan", "time_enter_scan")))
    except KeyboardInterrupt:
        logging.info("Extinction de Blueberry")
        exit
