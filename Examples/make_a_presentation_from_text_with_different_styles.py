#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Each line of the text becomes a slide of the presentation, we change of style
depending on the length of text line.
"""
import sys

# Import from lpod
from lpod.document import odf_new_document
from lpod.frame import odf_create_text_frame
from lpod.draw_page import odf_create_draw_page
from lpod.style import odf_create_style

encoding = "utf8"

#lst = open(sys.argv[1]).readlines()

lst="""123
azertyuiop
azertyuiop azertyuiop
azertyuiop azertyuiop azertyuiop
azertyuiop azertyuiop azertyuiop azertyuiop
azertyuiop azertyuiop azertyuiop azertyuiop azertyuiop
azertyuiop azertyuiop azertyuiop azertyuiop azertyuiop azertyuiop
azertyuiop azertyuiop azertyuiop azertyuiop azertyuiop azertyuiop azertyuiop
azertyuiop azertyuiop azertyuiop azertyuiop azertyuiop azertyuiop azertyuiop azertyuiop
azertyuiop azertyuiop azertyuiop azertyuiop azertyuiop azertyuiop azertyuiop azertyuiop azertyuiop
end.
""".splitlines()

output_filename = "my_generated_presentation.odp"

presentation = odf_new_document('presentation')

presentation_body = presentation.get_body()

# Creating a smooth style for the graphic item
base_style = odf_create_style (
                    'graphic',
                    name='Gloup48',
                    parent="standard",
                    stroke="none",
                    fill_color="#b3b3b3",
                    textarea_vertical_align="middle",
                    padding_top="1cm",
                    padding_bottom="1cm",
                    padding_left="1cm",
                    padding_right="1cm",
                    line_distance="0cm",
                    guide_overhang="0cm",
                    guide_distance="0cm",
                    )
base_style.set_properties(area='paragraph', align='center')
base_style.set_properties(
                    area='text',
                    color="#dd0000",
                    text_outline="false",
                    font=u"Liberation Sans",
                    font_family=u"Liberation Sans", # compatibility
                    font_style_name="Bold",
                    family_generic="swiss",
                    size="48pt",
                    weight="bold"
                    )

presentation.insert_style(base_style)

# Making o lot of variations
variants = [10,11,14,16,20,24,32,40,44]
text_sz =  [95,80,65,50,40,30,20,10,5]
for size in variants:
    variant_style = base_style.clone()
    variant_style.set_attribute('style:name', 'Gloup%s' % size)
    variant_style.set_properties(
                    area = 'text',
                    size = "%spt" % size )
    presentation.insert_style(variant_style)

count = 0

for blurb in lst:
    count += 1
    text = blurb.decode(encoding)
    name = u"%s - %s" % (count, text[:10])
    page = odf_create_draw_page(name)
    # choosing some style:
    size = 48
    for i, max_size in enumerate(text_sz):
        if len(text) > max_size:
            size = variants[i]
            break

    text_frame = odf_create_text_frame(
        text,
        size = ('24cm', '2cm'),
        position = ('2cm', '8cm'),
        style = 'Gloup%s' % size,
        text_style = 'Gloup%s' % size)

    page.append(text_frame)
    presentation_body.append(page)

presentation.save(target=output_filename, pretty=True)
