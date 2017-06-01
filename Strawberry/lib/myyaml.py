#!/usr/bin/python3

import logging
import yaml


class myyaml(dict):

    def read(self, fichier):
        try:
            with open(fichier, "r") as outline:
                self = yaml.load(outline)
        except Exception as e:
            logging.error("Erreur lors de la lecture du fichier yaml. Message d'erreur: " + str(e))


    def write(self, fichier):
        try:
            with open(fichier, "w") as outline:
                #json_data = yaml.dumps(self, ensure_ascii=False)
                yaml.dump(dict(self), outline, indent=4, default_flow_style=False, allow_unicode=False)
        except Exception as e:
            logging.error("Erreur lors de l'ecriture du fichier yaml. Message d'erreur: " + str(e))

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
