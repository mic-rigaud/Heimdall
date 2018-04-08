# @Author: michael
# @Date:   07-Apr-2018
# @Filename: ping_scan.py
# @Last modified by:   michael
# @Last modified time: 08-Apr-2018
# @License: GNU GPL v3

#!/usr/bin/python3

import datetime
import ipaddress
import logging
import os
import re
import subprocess
import threading

import netifaces as ni

from application.src.api.api_bdd import *
from application.src.api.api_telegram import ApiTelegram

FNULL = open(os.devnull, 'w')
INTERFACE = "wlp3s0"
NETWORKSTATUS = {}


class PingScan(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global INTERFACE
        INTERFACE = Parametre.get(Parametre.section == "interface",
                                  Parametre.key == "interface").value

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
        ping_return = self.ping(str(self.host))
        record = Ip.select().where((Ip.ip == str(self.host)) & (Ip.mac == mac))
        record_null = Ip.select().where((Ip.ip == str(self.host)) &
                                        (Ip.mac == "NULL"))
        if ping_return and not record.exists():
            if ping_return and record_null.exists():
                element = record_null.get()
                element.mac = mac
                element.time_last = datetime.datetime.now()
                element.save()
            else:
                Ip.create(ip=str(self.host), mac=mac).save()
                send_alert(str(self.host), mac)
        elif ping_return and record.exists():
            element = record.get()
            element.time_last = datetime.datetime.now()
            element.save()
        elif not ping_return and record.exists():
            element = record.get()
            element.satus = False
            element.save()

    def ping(self, hostname):
        commande = "ping -c 1 " + hostname
        response = subprocess.call(commande, shell=True, stdout=FNULL)
        return bool(response == 0)


def send_alert(ip, mac):
    alert_type = Parametre.get(Parametre.section == "alert",
                               Parametre.key == "alert_type")
    if alert_type == "telegram":
        telegram_token = Parametre.get(Parametre.section == "telegram",
                                       Parametre.key == "token")
        telegram_chat_id = Parametre.get(Parametre.section == "telegram",
                                         Parametre.key == "chat_id")
        ApiTelegram(telegram_token.value).send_alert(
            "Un nouveau peripherique " +
            "qui n est pas de confiance s est connecte \n" +
            "  ip : {} \n  mac : {}".format(ip, mac), telegram_chat_id.value)


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


def get_addr():
    try:
        resultat = ni.ifaddresses(INTERFACE)[2][0]['addr']
    except:
        logging.exception(
            "Erreur lors de la recherche de l'adresse ip. Probablement une erreur de configuration. L'interface d'écoute ne doit pas etre "
            + INTERFACE)
        print("=== ERREUR ===")
        exit()
    return resultat


def get_netmask():
    return ni.ifaddresses(INTERFACE)[2][0]['netmask']


def liste_address():
    adresse = get_addr() + "/" + get_netmask()
    net = ipaddress.IPv4Interface(adresse)
    return net.network.hosts()
