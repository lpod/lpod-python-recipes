# -*- coding: UTF-8 -*-
from lpod.document import odf_new_document
from lpod.paragraph import odf_create_paragraph

document = odf_new_document('text')
body = document.get_body()

# we knwo we have a style of name "highlight" :

body.append(odf_create_paragraph(
        u'Highlighting the word',
        style = 'highlight'))
