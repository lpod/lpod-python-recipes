#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ok lpod 1.0
import os

# Some utilities
import urllib
def random_text(sentences):
    uri = "http://enneagon.org/phrases/%s" % sentences
    try:
        text = urllib.urlopen(uri).read().decode("iso8859-1")
    except:
        text = u"Almost no text."
    return text

# 0 - Import from lpod
from lpod.document import odf_new_document
from lpod.heading import odf_create_heading
from lpod.paragraph import odf_create_paragraph

# 1 - Create the document
my_document = odf_new_document('text')
# Now document is an empty text document issued from a template. It’s a
# bit like creating a new text document in your office application,
# except lpOD templates don’t create a default paragraph.

# 2 - Adding Content
# Contents go into the body
body = my_document.get_body()
# Now we have a context to attach new elements to. In a text document, we
# generally want to write paragraphs, lists, headings, and a table of
# content to show the document hierarchy at first.

# 2.1 - Adding Main Title
# Titles are organised by level, starting from level 1.
#So let’s add the main title of our document:
title1 = odf_create_heading(1, random_text(1)[:70])
body.append(title1)

# 2.2 - Adding more Titles and Paragraphs
for p in range(3):
    # title of second level:
    title = odf_create_heading(2, random_text(1)[:70])
    body.append(title)

    # Adding a basic Paragraph of plain text
    paragraph = odf_create_paragraph(random_text(10))
    body.append(paragraph)


if not os.path.exists('test_output'):
    os.mkdir('test_output')

output = os.path.join('test_output', 'my_basic_text_document.odt')

# 3 - Saving Document
# Last but not least, don’t lose our hard work:
my_document.save(target=output, pretty=True)
# The pretty parameter asks for writing an indented serialized XML.
# The cost in space in negligible and greatly helps debugging,
# so don’t hesitate to use it.
