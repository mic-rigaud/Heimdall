#!/usr/bin/python3

import subprocess
import os
import threading
import netifaces as ni
import logging
import ipaddress
import time
import re

FNULL = open(os.devnull, 'w')
INTERFACE = 'wlan0'

NETWORKSTATUS = {}

class Scan(threading.Thread):
    def __init__(self, database):
        threading.Thread.__init__(self)
        self.myDatabase = database

    def run(self):
        scan(self.myDatabase)

class Ping(threading.Thread):
    '''
    Ping: Cette classe permet de realiser les ping sur les differents host
    '''
    def __init__(self, host, database):
        threading.Thread.__init__(self)
        self.host = host
        self.myDatabase = database

    def run(self):
        mac = get_mac(str(self.host))
        ping_return = ping(str(self.host))
        my_time = time.asctime( time.localtime(time.time()) )
        record = self.myDatabase.get_record_from_ip_mac(str(self.host), mac)
        if ping_return and record == "":
            self.myDatabase.add_record(str(self.host), mac, my_time, "NON", "ACTIF")
        elif ping_return and record != "":
            self.myDatabase.update_record(record[0], str(self.host), mac, my_time, "NON", "ACTIF")
        elif not ping_return and record != "":
            self.myDatabase.update_record(record[0], str(self.host), mac, my_time, "NON", "PLUS_ACTIF")

def get_mac(hostname):
    if hostname == get_addr():
        return "MON_ADRESSE"
    commande = "arp -n " + hostname
    logging.info(commande)
    try:
        s = str(subprocess.check_output(commande, shell=True))
        logging.info(s)
        a = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", s)
        if a == None:
            return "NULL"
        logging.info(a)
        return re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", s).groups()[0]
    except subprocess.CalledProcessError:
        return ""

def ping(hostname):
    commande = "ping -c 1 " + hostname
    response = subprocess.call(commande, shell=True, stdout=FNULL)
    return bool(response == 0)

def get_addr():
    return ni.ifaddresses(INTERFACE)[2][0]['addr']

def get_netmask():
    return ni.ifaddresses(INTERFACE)[2][0]['netmask']

def liste_address():
    adresse = get_addr() + "/" + get_netmask()
    net = ipaddress.IPv4Interface(adresse)
    return net.network.hosts()


def scan(database):
    for adresse in liste_address():
        mythread = Ping(adresse, database)
        mythread.start()
