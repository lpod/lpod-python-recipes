# -*- coding: UTF-8 -*-
# Let's add another section to make our document clear:
# Annotations are notes that don’t appear in the document but typically on a
# side bar in a desktop application. So they are not printed.
from lpod.document import odf_new_document
from lpod.paragraph import odf_create_paragraph

from lpod.heading import odf_create_heading

document = odf_new_document('text')
body = document.get_body()

body.append(odf_create_heading(1, u"Annotations"))
paragraph = odf_create_paragraph(u"A paragraph with an annotation in the middle.")
body.append(paragraph)

# Annotations are inserted like notes but they are simpler:

paragraph.insert_annotation(after=u"annotation",
        body=u"It's so easy!", creator=u"Luis")

# Annotation arguments are quite different:
# after   =>  The word after what the annotation is inserted.
# body    =>  The annotation itself, at the end of the page.
# creator =>  The author of the annotation.
# date    =>  A datetime value, by default datetime.now().
