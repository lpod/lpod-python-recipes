#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ok lpod 1.0
"""
Create a table of 1000 lines and 100 columns, extract a sub table of 100 lines
26 columns, save the result in a spreadsheet document.
"""
import os

# Import from lpod
from lpod.document import odf_new_document
from lpod.table import odf_create_table, odf_create_row, odf_create_cell

def suite(n):
    if n % 2 == 0:
        return n / 2
    return 3 * n + 1

if __name__=="__main__":
    spreadsheet = odf_new_document('spreadsheet')

    # Populate the table in the spreadsheet
    body = spreadsheet.get_body()
    table = odf_create_table(u"Big Table")
    body.append(table)

    lines = 1000
    cols = 100

    for line in range(lines):
        row = odf_create_row()
        values = []
        n = line
        for i in range(cols):
            values.append(n)
            n = suite(n)
        row.set_values(values)
        table.append(row)

    print "Size of Big Table :", table.get_size()

    # now extract 100 rows of 26 columns :
    table1 = odf_create_table(u"Extract 1")
    for r in range(800,900):
        row = table.get_row(r)
        values = [ row.get_value(x) for x in xrange(50,76) ]
        row2 = odf_create_row()
        row2.set_values(values)
        table1.append(row2)
    body.append(table1)

    print "Size of extracted table 1 :", table1.get_size()

    # other method
    table2 = odf_create_table(u"Extract 2")
    cells = table.get_cells( coord=(50, 800, 75, 899) )
    table2.set_cells(coord=(2, 3), cells=cells)
    body.append(table2)

    print "Size of extracted table 2 :", table2.get_size()

    if not os.path.exists('test_output'):
        os.mkdir('test_output')

    output = os.path.join('test_output', "my_big_spreadsheet.ods")

    spreadsheet.save(target=output, pretty=True)

    expected_result = """
Size of Big Table : (100, 1000)
Size of extracted table 1 : (26, 100)
Size of extracted table 2 : (26, 100)
"""
