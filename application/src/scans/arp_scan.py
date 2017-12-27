#!/usr/bin/python3

import subprocess
import os
import threading
import netifaces as ni
import logging
import ipaddress
import datetime
import re

from application.src.api.api_telegram import ApiTelegram
from application.src.api.api_bdd import *

FNULL = open(os.devnull, 'w')

NETWORKSTATUS = {}

class ArpScan(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global INTERFACE
        INTERFACE = Parametre.get(Parametre.section == "interface",
                                  Parametre.key == "interface").value

    def run(self):
        print("hello")
