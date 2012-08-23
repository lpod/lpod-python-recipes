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

doc = odf_get_document(filename)

# The body object is an XML element from which we can access one or several
# other elements we are looking for.
body = doc.get_body()

# Accessing a list of elements
# Should you need to access all elements of a kind, there are the
# get_xxxs methods, where xxx can be paragraph, heading, list, table, etc.
print "%s get methods are available" % (' '.join(dir(body)).count('get_'))
# Some examples, that you cant check against actual content of the odt file:
# See how complex is our wikipedia documents:
print "number of headings:", len(body.get_headings())
print "number of images stored:", len(body.get_images())
print "number of paragraphs:", len(body.get_paragraphs())
print "number of links (URLs):", len(body.get_links())
print "number of footnotes:", len(body.get_notes())
# Our sampledocument has no table:
print "number of tables:", len(body.get_tables())

# Each get_xxx_list method provides parameters for filtering the results.
# For example headings can be listed by level, annotations by creator, etc.
# Almost all of them accept filtering by style and content using a regular
# expressions.
print "Paragraphs with 'Fish':", len(body.get_paragraphs(content=r'Fish'))
print "Paragraphs with 'answer' and '42':", len(body.get_paragraphs(
    content=r'answer.*42'))

Expected_result = """
114 get methods are available
number of headings: 29
number of images stored: 0
number of paragraphs: 175
number of links (URLs): 361
number of footnotes: 49
number of tables: 0
Paragraphs with 'Fish': 4
Paragraphs with 'answer' and '42': 1
"""
