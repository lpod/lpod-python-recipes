#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ok lpod 1.0

# Uncommented parts are explained in : create_a_basic_text_document.py

# Imports from lpod
from lpod.document import odf_new_document
# Import the list module
from lpod.list import odf_create_list
# Import the list item factory module
from lpod.list import odf_create_list_item

# Create the document
my_document = odf_new_document('text')
body = my_document.get_body()

# Adding List
my_list = odf_create_list([u'Arthur', u'Ford', u'Trillian'])
# The list factory accepts a Python list of unicode strings and list items.

# The list can be written even though we will modify it afterwards:
body.append(my_list)

# Adding more List Item to the list, using the factory
item = odf_create_list_item(u'Marvin')
my_list.append_item(item)

# And finally save the document.
my_document.save(target='my_document_with_list.odt', pretty=True)

# it should contain only :
print my_document.get_formatted_text()
# - Arthur
# - Ford
# - Trillian
# - Marvin
