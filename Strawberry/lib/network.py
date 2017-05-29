#!/usr/bin/python3

import subprocess
import os
import threading
import netifaces as ni
import ipaddress


FNULL = open(os.devnull, 'w')
INTERFACE = 'wlan0'

NETWORKSTATUS = {}

class Ping(threading.Thread):
    '''
    Ping: Cette classe permet de realiser les ping sur les differents host
    '''
    def __init__(self, host):
        threading.Thread.__init__(self)
        self.host = host

    def run(self):
        if ping(str(self.host)):
            NETWORKSTATUS[str(self.host)] = True

def ping(hostname):
    commande = "ping -c 1 " + hostname
    response = subprocess.call(commande, shell=True, stdout=FNULL)
    return bool(response == 0)

def getAddr():
    return ni.ifaddresses(INTERFACE)[2][0]['addr']

def getNetmask():
    return ni.ifaddresses(INTERFACE)[2][0]['netmask']

def liste_address():
    adresse = getAddr() + "/" + getNetmask()
    net = ipaddress.IPv4Interface(adresse)
    return net.network.hosts()


def scan():
    for adresse in liste_address():
        mythread = Ping(adresse)
        mythread.start()
    return NETWORKSTATUS
