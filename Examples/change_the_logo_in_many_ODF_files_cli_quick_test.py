#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
just for testing
"""
import os

command = "python change_the_logo_in_many_ODF_files_cli.py \
          -o oldlogo.png -n newlogo.png  logo_in* "

os.system(command)
