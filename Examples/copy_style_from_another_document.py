#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ok lpod 1.0
# Import from lpod
from lpod.document import odf_get_document

# ODF export of Wikipedia article Hitchhiker's Guide to the Galaxy (CC-By-SA)
filename = "collection2.odt"

# For convenience we use some remote access to the document
#from urllib2 import urlopen
#filename = urlopen("http://arsaperta.org/collection2.odt")

style_filename = "lpod_styles.odt"  # from the LPOD package

# We want to change the styles of the collection2.odt.
# We know the lpod_styles.odt document contains an interesting style.
# So let’s first fetch the style:
style_document = odf_get_document(style_filename)

# Open our document:
document = odf_get_document(filename)

# We could change only some styles, but here we want a clean basis:
document.delete_styles()

# And now the actual style change:
document.merge_styles_from(style_document)

# Saving the document (with a different name)
document.save(target="my_collection_styled.odt", pretty=True)

################################################################################
# For more advanced version, see the lpod-style.py script in the lpod library  #
################################################################################
