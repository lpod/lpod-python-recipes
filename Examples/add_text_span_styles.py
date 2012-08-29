#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ok lpod 1.0
"""
Transform a not styled document into a multi styled document, by changing size and color of each parts of words.
"""
import sys, os
from struct import unpack
# Import from lpod
from lpod.style import odf_create_style
from lpod.document import odf_get_document

def get_default_doc():

    default = "dormeur_notstyled.odt"
    # For convenience we use some remote access to the document
    #from urllib2 import urlopen
    #default = urlopen("http://arsaperta.org/dormeur_notstyled.odt")
    return default

def style_name():
    "returns a random style name"
    return 'rnd%s' %  (unpack("H",os.urandom(2))[0]/1024)

if __name__=="__main__":
    try:
        source = sys.argv[1]
    except IndexError:
        source = get_default_doc()

    document = odf_get_document(source)
    body = document.get_body()

    print "Add some span styles to", source
    # create some random text styles
    for i in range(64):
        style = odf_create_style (
                        'text',
                        name = 'rnd%s' % i,
                        color = "#%x" % (unpack("I",os.urandom(4))[0] / 256),
                        size = "%s" % (8+i/5),
                        )
        document.insert_style(style)

    words = set(body.get_text(True).split())
    for word in words:
        name = style_name()
        style = document.get_style('text', name)
        for paragraph in body.get_paragraphs() + body.get_headings():
            # apply style to each text matching with the regex of some word
            paragraph.set_span(name, regex=word)

    if not os.path.exists('test_output'):
        os.mkdir('test_output')

    output = "my_span_styled_" + source
    document.save( target=os.path.join('test_output', output),  pretty=True)
