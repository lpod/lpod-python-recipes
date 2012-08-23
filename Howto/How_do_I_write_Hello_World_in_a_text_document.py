# -*- coding: UTF-8 -*-
#  I want to write "Hello World" on the first page.

from lpod.document import odf_new_document
from lpod.paragraph import odf_create_paragraph

document = odf_new_document('text')
body = document.get_body()
paragraph = odf_create_paragraph(u"Hello World")
body.append(paragraph)
