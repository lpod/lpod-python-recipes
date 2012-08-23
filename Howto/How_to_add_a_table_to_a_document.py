# -*- coding: UTF-8 -*-
from lpod.document import odf_new_document
from lpod.heading import odf_create_heading
from lpod.paragraph import odf_create_paragraph

document = odf_new_document('text')
body = document.get_body()

# Let's add another section to make our document clear:

body.append(odf_create_heading(1, u"Tables"))
body.append(odf_create_paragraph(u"A 3x3 table:"))

# Creating a table :

from lpod.table import odf_create_table
table = odf_create_table(u"Table 1", width=3, height=3)
body.append_element(table)
