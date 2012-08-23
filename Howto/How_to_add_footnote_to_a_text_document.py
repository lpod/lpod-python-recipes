# -*- coding: UTF-8 -*-
from lpod.document import odf_new_document
from lpod.paragraph import odf_create_paragraph

document = odf_new_document('text')
body = document.get_body()

paragraph = odf_create_paragraph(u"A paragraph with a footnote "
        u"about references in it.")
body.append(paragraph)

# Notes are quite complex so they deserve a dedicated API on paragraphs:

paragraph.insert_note(after=u"graph", note_id='note1', citation=u"1",
        body=(u'Author, A. (2007). "How to cite references", '
              u'New York: McGraw-Hill.'))

# That looks complex so we detail the arguments:
#
# after    =>   The word after what the “¹” citation is inserted.
# note_id  =>	The unique identifier of the note in the document.
# citation => 	The symbol the user sees to follow the footnote.
# body 	   =>   The footnote itself, at the end of the page.
#
# LpOD creates footnotes by default. To create endnotes (notes
# that appear at the end of the document), give the
# note_class=’endnote’ parameter.
