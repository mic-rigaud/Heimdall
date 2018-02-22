# @Author: michael
# @Date:   22-Feb-2018
# @Project: Blueberry
# @Last modified by:   
# @Last modified time: 22-Feb-2018
# @License: GNU GPL v3



import logging
import configparser
import time

logging.basicConfig(filename='./logs/blueberry.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


from application.application import *


if __name__ == "__main__":
    main()
