# @Author: michael
# @Date:   26-Feb-2018
# @Project: Blueberry
# @Filename: local_app.py
# @Last modified by:   michael
# @Last modified time: 08-Apr-2018
# @License: GNU GPL v3

import os
import sys

from app_factory import create_app

sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.getcwd())

if __name__ == '__main__':
    app = create_app()

    app.run('localhost', 35000, debug=True)
