#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
 Strawberry
  auteurs: michael
  version: 0.1
  date: 13/05/2017
'''

import logging
import time
from Strawberry.lib import network
from Strawberry.lib import myjson

logging.basicConfig(filename='/home/michael/Documents/Programation/Strawberry/log/heimdall.log',
                    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

NETWORKSTATUS = myjson.myjson()
NETWORKSTATUS.read("monjson.json")

def main():
    logging.info("Démarage du service")
    a=0
    while a<100:
        network_status = network.scan()
        NETWORKSTATUS.load(network_status)
        NETWORKSTATUS.write("monjson.json")
        a=a+1
        time.sleep(1)
    logging.info("Fin du service")


if __name__=="__main__":
    main()
