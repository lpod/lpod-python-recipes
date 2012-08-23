#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Create some color chart in a spreadsheet using cells styles.
(taken from the LPOD library test cases)
"""

# Import from the Standard Library
from os import mkdir
from os.path import join, exists

# Import from lpod
from lpod import __version__, __installation_path__
from lpod.document import odf_new_document
from lpod.table import odf_create_cell, odf_create_row
from lpod.table import odf_create_table
from lpod.style import odf_create_table_cell_style
from lpod.style import make_table_cell_border_string
from lpod.style import odf_create_style, rgb2hex

# Hello messages
print 'lpod installation test'
print ' Version           : %s' %  __version__
print ' Installation path : %s' % __installation_path__
print
print 'Generating color chart in my_color_chart.ods ...'


document = odf_new_document('spreadsheet')
body = document.get_body()
table = odf_create_table(u'chart')

for y in xrange(0, 256, 8):
    row = odf_create_row()
    for x in xrange(0, 256, 32):
        cell_value = (x, y, (x+y) % 256 )
        border_rl = make_table_cell_border_string(
                                thick = '0.20cm',
                                color = 'white'
                                )
        border_bt = make_table_cell_border_string(
                                thick = '0.80cm',
                                color = 'white',
                                )
        style = odf_create_table_cell_style(
                                color = 'grey' ,
                                background_color = cell_value,
                                border_right = border_rl,
                                border_left = border_rl,
                                border_bottom = border_bt,
                                border_top = border_bt,
                                )
        name = document.insert_style(style=style, automatic=True)
        cell = odf_create_cell(value=rgb2hex(cell_value), style=name)
        row.append_cell(cell)
    table.append_row(row)

    row_style = odf_create_style('table-row', height='1.80cm')
    name_style_row = document.insert_style(style=row_style, automatic=True)
    for idx,row in table.get_rows():
        row.set_style(name_style_row)
        table.set_row(row.y, row)

    col_style = odf_create_style('table-column', width='3.6cm')
    name = document.insert_style(style=col_style, automatic=True)
    for idx, column in table.get_columns():
        column.set_style(col_style)
        table.set_column(idx, column)

body.append(table)

document.save("my_color_chart.ods", pretty=True)
