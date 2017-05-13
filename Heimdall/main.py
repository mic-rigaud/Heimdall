#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
 Heimdall
  auteurs: michael
  version: 0.1
  date: 13/05/2017
'''

import logging
import threading
from Heimdall.lib import network
from Heimdall.lib import myjson

logging.basicConfig(filename='/home/michael/Documents/Programation/Heimdall/log/heimdall.log',
                    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

NETWORKSTATUS = {}


class Ping(threading.Thread):
    '''
    Ping: Cette classe permet de réaliser les ping sur les différents host
    '''
    def __init__(self, host):
        threading.Thread.__init__(self)
        self.host = host

    def run(self):
        if network.ping(str(self.host)):
            NETWORKSTATUS[str(self.host)] = True


def main():
    logging.info("Démarage du service")
    for adresse in network.liste_address():
        th = Ping(adresse)
        th.start()
    myjson.write("monjson.json",NETWORKSTATUS)


if __name__=="__main__":
    main()
