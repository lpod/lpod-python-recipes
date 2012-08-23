# -*- coding: UTF-8 -*-
#  Adding a table of content to an existing text document.
from lpod.document import odf_new_document
from lpod.paragraph import odf_create_paragraph

document = odf_new_document('text')
body = document.get_body()

# The TOC element comes from the toc module
#

from lpod.toc import odf_create_toc

toc = odf_create_toc()
body.append(toc)
