#!/usr/bin/python3

import json
import logging

class myjson(dict):

    def read(self, fichier):
        try:
            with open(fichier, "r") as outline:
                self = json.loads(outline)
        except Exception as e:
            logging.error("Erreur lors de la lecture du fichier json. Message d'erreur: " + str(e))


    def write(self, fichier):
        try:
            with open(fichier, "w") as outline:
                json_data = json.dumps(self, ensure_ascii=False)
                json.dump(json_data, outline)
        except Exception as e:
            logging.error("Erreur lors de l'ecriture du fichier json. Message d'erreur: " + str(e))

    def load(self, json_in):
        self.add_new_network(json_in)
        self.remove_old_network(json_in)

    def add_new_network(self, json_in):
        for network in json_in:
            self[network] = True

    def remove_old_network(self, json_in):
        copy = self.copy()
        for network in copy:
            if not network in json_in:
                self.pop(network)
