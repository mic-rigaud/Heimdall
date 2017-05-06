import os
import sys
import subprocess
import logging
from lib import network

##############################################################################################################
# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('log/hello.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
##############################################################################################################

def osCheckCall(commande):
    try:
        return subprocess.check_call(commande, shell=True)
    except:
        logger.critical("Erreur lors de la commande: " + commande)






def main():
    logger.info("Initialisation du service")
    print('--------------------')
    for adresse in network.liste_address():
        print(adresse)
    if network.ping("192.168.1.1"):
        print("OK")
    else:
        print("pas ok")


if __name__=="__main__":
    main()
