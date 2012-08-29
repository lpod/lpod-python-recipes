#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
just for testing
"""

import os

if not os.path.exists('test_output'):
    os.mkdir('test_output')

command = 'cp -f presentation_logo.odp test_output ; \
          python ./add_logo_on_presentation.py -i newlogo.png -r 1-8 -s 4.00 \
          test_output/presentation_logo.odp '

os.system(command)
