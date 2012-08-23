#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
just for testing
"""
import os

command = ' python ./accessibility_insert_title_description_cli.py \
    -i test_title_description/newlogo.png \
    -t "New Logo" \
    -d "new logo with blue background" \
    test_title_description/ '

os.system(command)
