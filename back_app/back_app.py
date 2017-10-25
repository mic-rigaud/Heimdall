#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Blueberry
  auteurs: michael
  version: 0.1
  date: 23/10/2017
'''

import logging
import time
import yaml
from Strawberry.lib import Network
from Strawberry.lib import myyaml
from Strawberry.lib import TtyUi
from Strawberry.lib import NetworkDatabase


logging.basicConfig(filename='./log/blueberry.log',
                    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
