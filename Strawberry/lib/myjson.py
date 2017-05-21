import json
import logging

def read(fichier):
    try:
        with open(fichier,"r") as outline:
            data = json.loads(outline)
        return data
    except Exception as e:
        logging.error("Erreur lors de la lecture du fichier json. Message d'erreur: " + str(e))


def write(fichier,data):
    try:
        with open(fichier, "w") as outline:
            jsonData = json.dumps(data,ensure_ascii=False)
            json.dump(jsonData, outline)
    except Exception as e:
        logging.error("Erreur lors de l'écriture du fichier json. Message d'erreur: " + str(e))
