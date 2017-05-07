#

import subprocess
import os
import netifaces as ni
import ipaddress

FNULL = open(os.devnull, 'w')
INTERFACE = 'wlan0'


def ping(hostname):
    commande = "ping -c 1 " + hostname
    response = subprocess.call(commande, shell=True, stdout=FNULL )
    if response == 0:
        return True
    else:
        return False


def addr():
    return ni.ifaddresses(INTERFACE)[2][0]['addr']

def netmask():
    return ni.ifaddresses(INTERFACE)[2][0]['netmask']

def liste_address():
    adresse = addr() + "/" + netmask()
    net = ipaddress.IPv4Interface(adresse)
    return net.network.hosts()
