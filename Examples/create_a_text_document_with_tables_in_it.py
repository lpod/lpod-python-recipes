#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ok lpod 1.0
"""
Build a basic commercial document, with numerical values displayed in both the
text and in a table.
"""
# Import from lpod
from lpod.document import odf_new_document
from lpod.heading import odf_create_heading
from lpod.paragraph import odf_create_paragraph
from lpod.list import odf_create_list, odf_create_list_item
from lpod.table import odf_create_table, odf_create_row, odf_create_cell

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
        item = odf_create_list_item(u"%-10s, price: %.2f €" % (product.name, product.price))
        product_list.append(item)

    title12 = odf_create_heading(2, u"Your command")
    body.append(title12)

    command = {0 : 1, 1 : 12, 2 : 3, 4 : 5 }

    # A table in the text document :
    table = odf_create_table(u"Table")
    body.append(table)
    row = odf_create_row()
    row.set_values([u"Product", u"Price", u"Quantity", u"Amount"])
    table.set_row(0,row)
    row_number = 0
    for item, quantity in command.iteritems():
        prod = catalog[item]
        row = odf_create_row()
        row.set_value(0, prod.name)
        cell = odf_create_cell()
        cell.set_value(prod.price, text = u"%.2f €" % prod.price, currency = u"EUR", cell_type="float")
        row.set_cell(1, cell)
        row.set_value(2, quantity)
        p = prod.price * quantity
        cell = odf_create_cell()
        cell.set_value(p, text = u"%.2f €" % p, currency = u"EUR", cell_type="float")
        row.set_cell(3, cell)
        row_number += 1
        table.set_row(row_number, row)

    cols = table.get_width()
    column = cols - 1

    row = odf_create_row()
    row.set_value(column - 1, u"Total")
    total = reduce(lambda x,y:x+y, table.get_column_values(column)[1:])
    cell = odf_create_cell()
    cell.set_value(total, text = u"%.2f €" % total, currency = u"EUR", cell_type="float")
    row.set_cell(column, cell)
    row_number += 1
    table.set_row(row_number, row)

    row = odf_create_row()
    row.set_value(column - 1, u"Total with tax")
    total *= (1 + tax_rate)
    cell = odf_create_cell()
    cell.set_value(total, text = u"%.2f €" % total, currency = u"EUR", cell_type="float")
    row.set_cell(column, cell)
    row_number += 1
    table.set_row(row_number, row)

    commercial.save(target="my_commercial.odt", pretty=True)

