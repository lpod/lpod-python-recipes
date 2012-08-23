#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ok lpod 1.0

# Uncommented parts are explained in: create_a_basic_text_document.py

# Some utilities
import urllib
def random_text(sentences):
    uri = "http://enneagon.org/phrases/%s" % sentences
    try:
        text = urllib.urlopen(uri).read().decode("iso8859-1")
    except:
        text = u"Almost no text."
    return text

# Imports from lpod
from lpod.document import odf_new_document
from lpod.heading import odf_create_heading
from lpod.paragraph import odf_create_paragraph
# Import the Table Of Content relevant module
from lpod.toc import odf_create_toc

# Create the document
my_document = odf_new_document('text')
body = my_document.get_body()

# Create the Table Of Content
toc = odf_create_toc()
# Changing the default "Table Of Content" Title :
toc.set_title("My Table of Content")

# Do not forget to add every components to the document:
body.append(toc)

# Add content (See Create_a_basic_document.py)
title1 = odf_create_heading(1, random_text(1)[:70])
body.append(title1)
for p in range(3) :
    title = odf_create_heading(2, random_text(1)[:70])
    body.append(title)
    paragraph = odf_create_paragraph(random_text(10))
    body.append(paragraph)

# Beware, update the TOC with the actual content. If not done there,
# the reader will need to "update the table of content" later.
toc.fill()

# And finally save the document.
my_document.save(target='my_document_with_toc.odt', pretty=True)
