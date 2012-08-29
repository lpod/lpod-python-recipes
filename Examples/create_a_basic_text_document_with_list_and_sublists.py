#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ok lpod 1.0
import os

# Uncommented parts are explained in : create_a_basic_document_with_a_list.py

# Imports from lpod
from lpod.document import odf_get_document, odf_new_document
# Import the list module
from lpod.list import odf_create_list
# Import the list item factory module
from lpod.list import odf_create_list_item

# Create the document
my_document = odf_new_document('text')
body = my_document.get_body()

# Adding List
my_list = odf_create_list([u'Arthur', u'Ford', u'Trillian'])
item = odf_create_list_item(u'Marvin')
my_list.append_item(item)
body.append(my_list)

# Adding Sublist¶
# A sublist is simply a list as an item of another list:
item.append(odf_create_list([u'Paranoid Android',u'older than the universe']))

# See the result:
print my_document.get_formatted_text()
# - Arthur
# - Ford
# - Trillian
# - Marvin
#   - Paranoid Android
#   - older than the universe


# Inserting List Item
# In case your forgot to insert an item:
my_list.insert_item(u'some dolphins', position=1)

# Or you can insert it before another item:
marvin = my_list.get_item(content=u'Marvin')
my_list.insert_item(u'Zaphod', before=marvin)
#Or after:
my_list.insert_item(u'and many others', after=marvin)


if not os.path.exists('test_output'):
    os.mkdir('test_output')

output = os.path.join('test_output', 'my_document_with_sublist.odt')

# And finally save the document.
my_document.save(target=output, pretty=True)

# See the result:
print my_document.get_formatted_text()
# - Arthur
# - some dolphins
# - Ford
# - Trillian
# - Zaphod
# - Marvin
#   - Paranoid Android
#   - older than the universe
# - and many others
