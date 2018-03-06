# Blueberry

## Description

Cet outil permet d'administrer un réseau local. Il permet de donner un aperçu de l'ensemble des machines présentes sur le réseau. A termes, cet outil donnera une interface d'administration web cartographiant le réseau et alertant lorsqu'il y aura un nouvel utilisateur dans le réseau. Une analyse par scan de port permettra de donner un niveau de sécurité des machines présentes.

Cet outil utilisera pour réaliser l'analyse:

- ping
- nmap
- arp

  Cet outil peut donc être considéré comme intrusif. Vérifié que vous avez bien l'accord de votre administrateur réseaux avant de déployer cet outil.

## Suivi de versions

Nous en sommes à la **version 0.1**.

### Objectifs pour la **version 1.0**:

- Outil en ligne de commande
- Analyser le réseau pour détecter toutes les machines présentes
- Enregistrer les machines présentes avec leur MAC et leur nom DNS
- Envoyer un mail lorsqu'une nouvelle machine est détectée

### Objectifs pour la **version 2.0**:

- Interface web permettant l'administration
- Cartographie du réseaux

### Objectifs pour la **version 3.0**:

- Analyser à la demande les machines sur le réseaux pour en connaître leur vulnérabilités
- Envoyer ce Bilan à l'administrateur du réseaux

## FAQ

### Pourquoi ce nom?

Ce nom a été choisi pour deux raisons:
- Premièrement, Blueberry à pour but d'être installé sur un raspberry. Et les gâteau aux myrtilles et aux framboises sont les meilleurs!
- Deuxièmement, ce logiciel doit chasser les intrus sur notre réseau. On peut voir le parallèle avec la BD de cow-boy de même nom... On va chasser les méchants!