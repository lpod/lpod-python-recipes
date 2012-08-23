# -*- coding: UTF-8 -*-
from lpod.document import odf_new_document
from lpod.table import odf_create_table

document = odf_new_document('spreadsheet')
body = document.get_body()

table = odf_create_table(u"Empty Table")
table.set_value('A1', "Hello World")
body.append(table)
