# -*- coding: UTF-8 -*-
from lpod.document import odf_new_document
from lpod.list import odf_create_list

document = odf_new_document('text')
body = document.get_body()

my_list = odf_create_list([u'chocolat', u'café'])

# In case your forgot to insert an important item:
my_list.insert_item(u"Chicorée", position=1)

# Or you can insert it before another item:
cafe = my_list.get_item(content = u"café")
my_list.insert_item(u'Chicorée', before=cafe)

# Or after:
my_list.insert_item(u"Chicorée", after=cafe)
