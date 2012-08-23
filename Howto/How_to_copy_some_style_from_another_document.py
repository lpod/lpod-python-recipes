# -*- coding: UTF-8 -*-
from lpod.document import odf_get_document, odf_new_document

document = odf_new_document('text')
body = document.get_body()

# Let's imagine the sample_styles.odt document contains an interesting style.
#
# So let’s first fetch the style:

try:
    lpod_styles = odf_get_document('sample_styles.odt')
    highlight = lpod_styles.get_style('text',
                        display_name=u"Yellow Highlight")
except IOError:
    # let's create some *very simple* text style.
    from lpod.style import odf_create_style
    highlight = odf_create_style('text',
                                display_name=u"Yellow Highlight",
                                color = 'blue',
                                italic = True)

# We made some assumptions here:
#
# ‘text’              :  The family of the style, text styles apply on individual characters.
# u”Yellow Highlight” : The name of the style as we see it in a desktop application.
# display_name        : Styles have an internal name (“Yellow_20_Highlight” in this example) but we gave the display_name instead.
#
# We hopefully have a style object that we add to our own collection:

document.insert_style(highlight, automatic=True)
