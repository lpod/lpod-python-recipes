#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ok for lpod v1.0
"""
Concatenate several presentations (including presentations found in sub
directories), possibly merge styles and images.
"""
import os
import sys
import optparse
from hashlib import sha1
import time
# Import from lpod
from lpod import ODF_MANIFEST
from lpod.document import odf_get_document, odf_new_document

default_concat_filename = "my_concat_presentation.odp"
known_files = set()
counter_odp = 0

def check_known(path):
    "remember already seen document with sha1 footprint"
    try:
        content = open(path).read()
    except IOError:
        return False
    footprint = sha1(content).digest()
    if footprint in known_files:
        return False
    known_files.add(footprint)
    return True

def parse_odp(path, dest_presentation):
    """ Using LPOD for:
            - open possible ODP document: odf_get_document
            - copy content and merge styles
    """
    lst = os.path.basename(path).split(".")
    suffix = lst[-1].lower()
    if suffix != "odp" :
        return
    # Check the document unicity
    if not check_known(path):
        return
    try:
        document = odf_get_document(path)
    except:
        return
    global counter_odp
    counter_odp += 1
    # merge styles
    dest_presentation.merge_styles_from(document)
    # add all slides
    dest_body = dest_presentation.get_body()
    dest_manifest = dest_presentation.get_part(ODF_MANIFEST)
    manifest = document.get_part(ODF_MANIFEST)
    slides = document.get_body().get_draw_pages()
    for slide in slides:
        slide = slide.clone()
        # dont forget images:
        for image in slide.get_images():
            uri = image.get_url()
            media_type = manifest.get_media_type(uri)
            dest_manifest.add_full_path(uri, media_type)
            dest_presentation.set_part(uri, document.get_part(uri))
        # append slide, expecting nothing good about its final style
        dest_body.append(slide)

if  __name__ == '__main__':

    usage = "usage: %prog [options] <ODP dirs>"
    description = "Concatenate the odp files in the path. Result for style may vary."
    parser = optparse.OptionParser(usage, description=description)
    parser.add_option("-o", "--output", dest="output", help="write output presentation to OUTPUT.",
                      action="store", type="string")
    options, sources = parser.parse_args()
    if not sources:
        print "need presentations sources !"
        parser.print_help()
        sys.exit(0)
    if options.output:
        concat_filename = options.output
    else:
        concat_filename = default_concat_filename

    t0 = time.time()
    # prepare destination file
    concat_presentation = odf_new_document('presentation')
    concat_presentation.delete_styles()

    for source in sources:
        if os.path.isdir(source):
            for root, dirs, files in os.walk(source):
                for name in files:
                    parse_odp(os.path.join(root, name), concat_presentation)
        else:
            parse_odp(source, concat_presentation)

    concat_presentation.save(target=concat_filename, pretty=True)
    elapsed = int(time.time() - t0)
    nb_slides = len(concat_presentation.get_body().get_draw_pages())
    print "%s presentations concatenated in %s (%s slides) in %ss." % (
        counter_odp, concat_filename, nb_slides, elapsed)
