#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ok lpod 1.0
"""
Transpose a table. Create a spreadsheet table (example: 50 rows and 20 columns), and subsequently
create a new table in a separate sheet where the columns and rows are now
swapped (e.g. 20 rows and 50 columns).
"""
# Import from lpod
from lpod.document import odf_new_document
from lpod.table import odf_create_table, odf_create_row

if __name__=="__main__":
    spreadsheet = odf_new_document('spreadsheet')

    # Populate the table in the spreadsheet
    body = spreadsheet.get_body()
    table = odf_create_table(u"Table")
    body.append(table)

    lines = 50
    cols = 20

    for line in range(lines):
        row = odf_create_row()
        for column in range(cols):
            row.set_value(column, "%s%s" % (chr(65 + column), line + 1))
        table.append(row)

    print "Size of Table :", table.get_size()

    table2 = odf_create_table(u"Symetry")

    # building the symetric table using classical method :
    for x in xrange(cols):
        values = table.get_column_values(x)
        table2.set_row_values(x, values)
    body.append(table2)

    # a more simple solution with the table.transpose() method :
    table3 = table.clone()
    table3.transpose()
    table3.set_name(u"Transpose")
    body.append(table3)

    print "Size of symetric table 2 :", table2.get_size()
    print "Size of symetric table 3 :", table3.get_size()

    spreadsheet.save(target="my_transposed_spreadsheet.ods", pretty=True)
