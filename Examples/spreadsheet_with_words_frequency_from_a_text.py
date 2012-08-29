#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ok lpod 1.0
"""
Load an ODF text, store the frequency of words in a spreadsheet, make requests
on the table, by regex or value.
"""
import sys
# Import from lpod
from lpod.document import odf_new_document
from lpod.table import odf_create_table, odf_create_row
from lpod.document import odf_get_document

def get_default_doc():

    default = "collection2.odt"

    # For convenience we use some remote access to the document
    #from urllib2 import urlopen
    #default = urlopen("http://arsaperta.org/collection2.odt")
    return default

if __name__=="__main__":
    try:
        source = sys.argv[1]
    except IndexError:
        source = get_default_doc()

    document_source = odf_get_document(source)
    spreadsheet = odf_new_document('spreadsheet')

    print "Word frequency analysis of", source
    text = document_source.get_body().get_text(recursive=True)
    for c in "():;!.,[]{}#@/\\=-_+*#@`\"'" :
        text = text.replace(c,' ')  # slow algorithm
    words = text.split()
    print "nb of words:", len(words)

    frequences = {}

    for word in words:
        frequences[word] = frequences.get(word, 0) + 1

    print "unique words found:", len(frequences)

    # Populate the table in the spreadsheet
    body = spreadsheet.get_body()
    table = odf_create_table(u"Frequency Table")
    body.append(table)

    sorted = [ (value, key) for key, value in frequences.iteritems() ]
    sorted.sort()
    sorted.reverse()

    # one solution :

    #for value, key in sorted:
    #    row = odf_create_row()
    #    row.set_value(0, key)
    #    row.set_value(1, value) # Cell type is guessed.
    #    table.append_row(row)

    # another solution :
    sorted = [ (k, v) for (v, k) in sorted ]
    table.set_values(sorted)

    print "rows in the table :", len(table.get_rows())

    # frequency of word:
    regex_query = "^the"
    print "Words corresponding to the regex:", regex_query
    result = table.get_rows(content = regex_query )
    for row in result:
        print "word: %-20s  occurences: %s" % (row.get_value(0), row.get_value(1))

    # list of words of frequecy = 15
    found = []
    for word, freq in table.iter_values():
        if freq == 15:
            found.append(word)
    print "list of words of frequency 15:", ", ".join(found)


    spreadsheet.save(target="my_frequency_spreadsheet.ods", pretty=True)

    expected_result = """
Word frequency analysis of collection2.odt
nb of words: 9128
unique words found: 2337
rows in the table : 2337
Words corresponding to the regex: ^the
word: the                   occurences: 644
word: they                  occurences: 15
word: their                 occurences: 11
word: then                  occurences: 10
word: there                 occurences: 7
word: these                 occurences: 4
word: them                  occurences: 4
word: themselves            occurences: 2
word: theme                 occurences: 2
word: themed                occurences: 1
word: theatrical            occurences: 1
list of words of frequency 15: two, they, release, one, its, his, film,
episodes, but, adaptation, UK, Radio, J, 0

"""
