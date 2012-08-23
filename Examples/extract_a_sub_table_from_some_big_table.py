#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ok lpod 1.0
"""
Create a table of 1000 lines and 100 columns, extract a sub table of 100 lines
26 columns, save the result in a spreadsheet document.
"""
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
    table2 = odf_create_table(u"Extract")
    for r in range(800,900):
        row = table.get_row(r)
        values = [ row.get_value(x) for x in xrange(50,76) ]
        row2 = odf_create_row()
        row2.set_values(values)
        table2.append(row2)
    body.append(table2)

    print "Size of extracted table :", table2.get_size()

    spreadsheet.save(target="my_big_spreadsheet.ods", pretty=True)

    expected_result = """
Size of Big Table : (100, 1000)
Size of extracted table : (26, 100)
"""
