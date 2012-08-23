#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ok lpod 1.0
# Import from lpod
from lpod.document import odf_get_document

# ODF export of Wikipedia article Hitchhiker's Guide to the Galaxy (CC-By-SA) :
filename = "collection2.odt"

# For convenience we can use some remote access to the document :

# from urllib2 import urlopen
# filename = urlopen("http://arsaperta.org/collection2.odt")
doc = odf_get_document(filename)

# The body object is an XML element from which we can access one or several
# other elements we are looking for.
body = doc.get_body()

# Should you be lost, remember elements are part of an XML tree:
mypara = body.get_paragraph(position = 42)
print "children of the praragraph:", mypara.get_children()
print "parent of the paragraph:", mypara.get_parent()

# And you can introspect any element as serialized XML:
link0 = body.get_link(position = 0)
print "Content of the serialization link:"
print link0.serialize()
print "which is different from the text content of the link:"
print link0.get_text(True)
