from background_task import background
from logging import getLogger
import threading
import netifaces as ni
import ipaddress
import subprocess
import time
import os
from Main_UI.models import NetworkDatabase
import re

logger = getLogger(__name__)

FNULL = open(os.devnull, 'w')
INTERFACE = 'eth0'


@background(schedule=60)
def demo_task(self, message):
    logger.debug('Scan Voici l execution de la tache planifier demo_task. message={0}'.format(message))


@background(schedule=60)
def scan():
    logger.debug('[SCAN] Debut du scan')
    for adresse in liste_address():
        mythread = Ping(adresse)
        mythread.start()

def test_scan():
    logger.debug('[SCAN] Debut du scan')
    for adresse in liste_address():
        mythread = Ping(adresse)
        mythread.start()


def get_addr():
    return ni.ifaddresses('eth0')[2][0]['addr']

def get_netmask():
    return ni.ifaddresses('eth0')[2][0]['netmask']

def liste_address():
    adresse = get_addr() + "/" + get_netmask()
    net = ipaddress.IPv4Interface(adresse)
    return net.network.hosts()


class Ping(threading.Thread):
    '''
    Ping: Cette classe permet de realiser les ping sur les differents host
    '''
    def __init__(self, host):
        threading.Thread.__init__(self)
        self.host = host

    def run(self):
        mac_ = get_mac(str(self.host))
        ping_return = self.ping()
        my_time = time.asctime( time.localtime(time.time()) )
        record = NetworkDatabase.objects.filter(ip=str(self.host), mac=mac_)
        if ping_return and not record.exists():
            NetworkDatabase(ip=str(self.host), mac=str(mac_), time_last=str(my_time), confiance="NON", statut="ACTIVE").save()
            logger.debug("[SCAN] Nouvelle enregistrement avec ip: {0} et mac: {1}".format(str(self.host), mac_))
        elif ping_return and record.exists():
            record[0].time=my_time
            record[0].statut="ACTIVE"
            record[0].save()
            logger.debug("[SCAN] Mise a jour avec ip: {0} et mac: {1}".format(str(self.host), mac_))
        elif not ping_return and record.exists():
            record[0].statut="NOT_ACTIVE"
            record[0].save()
            logger.debug("[SCAN] Mise a jour avec ip: {0} et mac: {1}".format(str(self.host), mac_))

    def ping(self):
        commande = "ping -c 1 " + str(self.host)
        response = subprocess.call(commande, shell=True, stdout=FNULL)
        return bool(response == 0)

def get_mac(hostname):
    if hostname == get_addr():
        return "MON_ADRESSE"
    commande = "arp -n " + hostname
    logger.debug(commande)
    try:
        s = str(subprocess.check_output(commande, shell=True))
        logger.debug(s)
        a = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", s)
        if a == None:
            return "NULL"
        logger.debug(a)
        return re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", s).groups()[0]
    except subprocess.CalledProcessError:
        return ""
