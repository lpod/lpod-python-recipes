#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ok lpod 1.0
"""
Create a new presentation from a previous one by extrating some slides, in a
different order.
"""
import sys
# Import from lpod
from lpod.document import odf_get_document, odf_new_document

filename = "presentation_base.odp"

# For convenience we use some remote access to the document
#from urllib2 import urlopen
#filename = urlopen("http://arsaperta.org/presentation_base.odp")
presentation_base = odf_get_document(filename)

output_filename = "my_extracted_slides.odp"


if __name__=="__main__":
    #extract = sys.argv[1:]
    extract = " 3 5 2 2"

    extracted = odf_new_document('presentation')

    body_base = presentation_base.get_body()
    body_extracted = extracted.get_body()

    # Important, copy styles too:
    extracted.delete_styles()
    extracted.merge_styles_from(presentation_base)

    for i in extract.split():
        try:
            slide_position = int(i) -1
            slide = body_base.get_draw_page(position = slide_position)
        except:
            continue
        if slide is None:
            continue

        slide = slide.clone()

        body_extracted.append(slide)

    extracted.save(target=output_filename, pretty=True)
