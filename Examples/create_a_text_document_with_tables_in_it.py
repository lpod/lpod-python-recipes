#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ok lpod 1.0
"""
Build a basic commercial document, with numerical values displayed in both the
text and in a table.
"""
import os

# Import from lpod
from lpod.document import odf_new_document
from lpod.heading import odf_create_heading
from lpod.paragraph import odf_create_paragraph
from lpod.list import odf_create_list, odf_create_list_item
from lpod.table import odf_create_table, odf_create_row, odf_create_cell
# for cell style
from lpod.style import odf_create_table_cell_style
from lpod.style import make_table_cell_border_string
from lpod.style import odf_create_style

# basic commercial document v1

class Product:
    def __init__(self, name, price):
        self.name = "Product %s" % name
        self.price = price

def make_catalog():
    cat_list = []
    price = 10.0
    for p in range(5):
        cat_list.append(Product(chr(65 + p), price))
        price += 10.5
    return cat_list

tax_rate = .196

if __name__=="__main__":
    commercial = odf_new_document('text')
    body = commercial.get_body()
    catalog = make_catalog()

    title1 = odf_create_heading(1, u"Basic commercial document")
    body.append(title1)
    title11 = odf_create_heading(2, u"Available products")
    body.append(title11)
    paragraph = odf_create_paragraph(u"Here the list:")
    body.append(paragraph)

    # List of products in a list :
    product_list = odf_create_list()
    body.append(product_list)
    for product in catalog:
        item = odf_create_list_item(u"%-10s, price: %.2f €" % (
                                            product.name, product.price))
        product_list.append(item)

    title12 = odf_create_heading(2, u"Your command")
    body.append(title12)

    command = {0 : 1, 1 : 12, 2 : 3, 4 : 5 }

    # A table in the text document :
    table = odf_create_table(u"Table")
    body.append(table)
    row = odf_create_row()
    row.set_values([u"Product", u"Price", u"Quantity", u"Amount"])
    table.set_row("A1", row)
    # or: table.set_row(0, row)
    row_number = 0
    for item, quantity in command.iteritems():
        prod = catalog[item]
        row = odf_create_row()
        row.set_value("A", prod.name)
        #or : row.set_value(0, prod.name)
        cell = odf_create_cell()
        cell.set_value(prod.price, text = u"%.2f €" % prod.price,
                                    currency = u"EUR", cell_type="float")
        row.set_cell("B", cell)
        #or : row.set_cell(1, cell)
        row.set_value("C", quantity)
        #row.set_value(2, quantity)
        p = prod.price * quantity
        cell = odf_create_cell()
        cell.set_value(p, text = u"%.2f €" % p,
                                    currency = u"EUR", cell_type="float")
        row.set_cell(3, cell)
        row_number += 1
        table.set_row(row_number, row)

    cols = table.get_width()
    column = cols - 1

    # add merged empty row
    row = odf_create_row()
    row_number += 1
    table.set_row(row_number, row)
    table.set_span((0, row_number, 3, row_number))

    # make total
    row = odf_create_row()
    row.set_value(column - 1, u"Total:")
    total = sum(table.get_column_values(column)[1:-1])
    cell = odf_create_cell()
    cell.set_value(total, text = u"%.2f €" % total,
                                currency = u"EUR", cell_type="float")
    row.set_cell(column, cell)
    row_number += 1
    table.set_row(row_number, row)


    # let merge some cells
    table.set_span((column -3, row_number, column -1, row_number), merge = True)

    row = odf_create_row()
    row.set_value(column - 1, u"Total with tax:")
    total *= (1 + tax_rate)
    cell = odf_create_cell()
    cell.set_value(total, text = u"%.2f €" % total,
                                currency = u"EUR", cell_type="float")
    row.set_cell(column, cell)
    row_number += 1
    table.set_row(row_number, row)
    # let merge some cells
    table.set_span((column -3, row_number, column -1, row_number), merge = True)

    # Let's add some style on first row
    border = make_table_cell_border_string(
                                thick = '0.03cm',
                                color = 'black'
                                )
    cell_style = odf_create_table_cell_style(
                                color = 'black',
                                background_color = (210, 210, 210),
                                border_right = border,
                                border_left = border,
                                border_bottom = border,
                                border_top = border,
                                )
    style_name = commercial.insert_style(style=cell_style, automatic=True)

    row = table.get_row(0)
    #for cell in row.get_cells(): #possible, but .traverse() is better
    for cell in row.traverse():
        cell.set_style(style_name)
        row.set_cell(x=cell.x, cell=cell)
    table.set_row(row.y, row)

    if not os.path.exists('test_output'):
        os.mkdir('test_output')

    output = os.path.join('test_output', "my_commercial.odt")

    commercial.save(target=output, pretty=True)
