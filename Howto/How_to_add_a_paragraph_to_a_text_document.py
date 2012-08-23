# -*- coding: UTF-8 -*-
from lpod.document import odf_new_document
from lpod.paragraph import odf_create_paragraph

document = odf_new_document('text')
body = document.get_body()

# create a new paragraph with some content :
paragraph = odf_create_paragraph(u"Hello_World")
body.append_element(paragraph)
