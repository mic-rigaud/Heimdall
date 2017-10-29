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
INTERFACE = 'wlan0'

NETWORKSTATUS = {}

class PingScan(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global INTERFACE
        INTERFACE = Parametre.get(Parametre.section == "interface",
                                  Parametre.key=="interface").value

    def run(self):
        for adresse in liste_address():
            mythread = Ping(adresse)
            mythread.start()

class Ping(threading.Thread):
    '''
    Ping: Cette classe permet de realiser les ping sur les differents host
    '''
    def __init__(self, host):
        threading.Thread.__init__(self)
        self.host = host

    def run(self):
        mac = get_mac(str(self.host))
        ping_return = ping(str(self.host))
        record = Ip.select().where((Ip.ip == str(self.host)) & (Ip.mac == mac))
        if ping_return and not record.exists():
            Ip.create(ip=str(self.host), mac=mac).save()
            telegram_token = Parametre.get(Parametre.section == "telegram" , Parametre.key == "token")
            telegram_chat_id = Parametre.get(Parametre.section == "telegram" , Parametre.key == "chat_id")
            ApiTelegram(telegram_token.value).send_alert("Un nouveau peripherique "+
            "qui n est pas de confiance s est connecte \n"+
            "  ip : {} \n  mac : {}".format(str(self.host), mac), telegram_chat_id.value)
        elif ping_return and record.exists():
            element = record.get()
            element.time_last = datetime.datetime.now()
            element.save()
        elif not ping_return and record.exists():
            element = record.get()
            element.satus = False
            element.save()


def get_mac(hostname):
    if hostname == get_addr():
        return "MON_ADRESSE"
    commande = "arp -n " + hostname
    try:
        s = str(subprocess.check_output(commande, shell=True))
        a = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", s)
        if a == None:
            return "NULL"
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
