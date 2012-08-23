# -*- coding: UTF-8 -*-
from lpod.document import odf_new_document

document = odf_new_document('text')
body = document.get_body()

# Lists are a dedicated object
from lpod.list import odf_create_list
my_list = odf_create_list([u'chocolat', u'café'])

# The list factory accepts a Python list of unicode strings and list items.
#
# The list can be written even though we will modify it afterwards:

body.append(my_list)
