# -*- coding: UTF-8 -*-
from lpod.document import odf_new_document

document = odf_new_document('text')
body = document.get_body()


from lpod.heading import odf_create_heading

title1 = odf_create_heading(1, u"The Title")
body.append(title1)
