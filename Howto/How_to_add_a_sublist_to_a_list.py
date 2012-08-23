# -*- coding: UTF-8 -*-
from lpod.document import odf_new_document
from lpod.list import odf_create_list

document = odf_new_document('text')
body = document.get_body()

my_list = odf_create_list([u'chocolat', u'café'])
body.append(my_list)

from lpod.list import odf_create_list_item

item = odf_create_list_item(u"thé")
my_list.append(item)

#A sublist is simply a list as an item of another list

item.append( odf_create_list( [u"thé vert", u"thé rouge"] ) )

print body.serialize(True)
