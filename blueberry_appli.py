#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Blueberry
  auteurs: michael
  version: 0.1
  date: 23/10/2017
'''

import logging
import configparser
import time

logging.basicConfig(filename='./logs/blueberry.log',
                    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


from application.application import *


if __name__=="__main__":
    main()
