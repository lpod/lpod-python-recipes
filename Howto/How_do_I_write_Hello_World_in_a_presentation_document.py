# -*- coding: UTF-8 -*-
# I want to write "Hello World" in the middle of the first page.

from lpod.document import odf_new_document
from lpod.frame import odf_create_text_frame
from lpod.draw_page import odf_create_draw_page

document = odf_new_document('presentation')
body = document.get_body()

page = odf_create_draw_page('page1', name=u"Page 1")
body.append(page)
text_frame = odf_create_text_frame([u"Hello", u"World"],
        size=('7cm', '5cm'), position=('11cm', '8cm'),
        style=u"colored", text_style=u"big")
