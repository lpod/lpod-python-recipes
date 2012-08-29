#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ok lpod 1.0
"""
Create a spreadsheet with one table.
"""
# Import from lpod
from lpod.document import odf_new_document
from lpod.table import odf_create_table

if __name__=="__main__":

    # creating an empty spreadsheet document:
    document = odf_new_document('spreadsheet')

    # Each sheet of a spreadsheet is a table:
    # setting drom the beginning width (columns) and height (rows)
    # is not mandatory, but a good practice, since lpod don't check
    # actual existence of cells
    body = document.get_body()
    table = odf_create_table(u"First Table", width = 20, height = 3)
    body.append(table)

    # A table contains rows, we can append some more.
    for r in range(2):
        table.append_row()
    print "rows in the table (3+2):", len(table.get_rows())

    #  A row contains cells
    for row in table.get_rows():
        print "row, nb of cells ", row.y,  len(row.get_cells())

    last_row = table.get_row(-1)
    print "nb of cells of the last row:", len(last_row.get_cells())

    # cell can have different kind of values
    for r in range(3):
        for c in range(10):
            table.set_value((c, r), u"cell %s %s"%(c, r))
    for r in range(3, 5):
        for c in range(10):
            table.set_value((c, r), c * 100 + r)

    # Before saving the document,  we can strip the unused colums:
    print "table size:", table.get_size()
    table.rstrip()
    print "table size after strip:", table.get_size()
    print "nb of cells of the last row:", len(table.get_row(-1).get_cells())
    print "Content of the table:"
    print table.to_csv()

    document.save(target="my_basic_spreadsheet.ods", pretty=True)
