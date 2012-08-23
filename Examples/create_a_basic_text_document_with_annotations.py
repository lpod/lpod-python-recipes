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

# Create the document
my_document = odf_new_document('text')
body = my_document.get_body()

# Add content (See Create_a_basic_document.py)
title1 = odf_create_heading(1, random_text(1)[:70])
body.append(title1)
for p in range(3):
    title = odf_create_heading(2, random_text(1)[:70])
    body.append(title)
    paragraph = odf_create_paragraph(random_text(10))

    # Adding Annotation
    # Annotations are notes that don’t appear in the document but
    # typically on a side bar in a desktop application. So they are not printed.

    # Now we add some annotation on each paragraph
    some_word = paragraph.get_text(True).split()[3]
    # choosing the 4th word of the paragraph to insert the note

    paragraph.insert_annotation(
        after = some_word,      # The word after what the annotation is inserted.
        body = u"It's so easy!", # The annotation itself, at the end of the page.
        creator = u"Bob"         # The author of the annotation.
        # date= xxx              A datetime value, by default datetime.now().
        )

    body.append(paragraph)

# And finally save the document.
my_document.save(target='my_document_with_annotations.odt', pretty=True)
