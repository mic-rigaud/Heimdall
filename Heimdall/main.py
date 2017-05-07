import os
import sys
import subprocess
import logging
from lib import network
import threading

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




class Ping(threading.Thread):
    def __init__(self,host):
        threading.Thread.__init__(self)
        self.host = host

    def run(self):
        if network.ping(str(self.host)):
            print(self.host)



def main():
    logger.info("Initialisation du service")
    print('--------------------')
    for adresse in network.liste_address():
        th = Ping(adresse)
        th.start()



if __name__=="__main__":
    main()
