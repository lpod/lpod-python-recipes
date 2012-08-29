#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ok lpod 1.0
"""
Insert a circle and a lot of lines (a fractal) in a text document.
"""
import os
import sys
import cmath
from math import sqrt

# Import from lpod
from lpod.document import odf_new_document
from lpod.heading import odf_create_heading
from lpod.shapes import odf_create_line, odf_create_ellipse
from lpod.paragraph import odf_create_paragraph

# some graphic computations
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def koch_split(self):
        c = self.a + 1.0/3.0 * (self.b -self.a)
        d = self.a + 2.0/3.0 * (self.b -self.a)
        m = 0.5 * (self.a + self.b)
        e = m + (d-c) * complex(0, -1)
        return [Vector(self.a, c), Vector(c, e), Vector(e, d),
                Vector(d, self.b)]

    def in_cm(self, val):
        if val == 0:
            m = self.a
        else:
            m = self.b
        return ("%.2fcm" % m.real, "%.2fcm" % m.imag)

def koch(vlist, cycle=2):
    if cycle <= 0:
        return vlist
    else:
        new_vlist = []
        for v in vlist:
            new_vlist.extend(v.koch_split())
        #del vlist
        return koch(new_vlist, cycle - 1)

def make_coords(side, vpos):
    orig = complex((17 - side)/2.0, vpos)
    v1 = Vector(orig, orig + complex(side, 0))
    v2 = Vector(v1.b, orig + cmath.rect(side, cmath.pi / 3))
    v3 = Vector(v2.b, orig)
    center = (v1.a + v1.b + v2.b) / 3
    vlist = koch([v1, v2, v3], cycle = 5)
    return center, vlist

if __name__=="__main__":

    document = odf_new_document('text')
    body = document.get_body()

    print "Making some Koch fractal"
    title = odf_create_heading(1, "Some Koch fractal")
    body.append(title)

    style = document.get_style('graphic')
    style.set_properties({"svg:stroke_color" : "#0000ff"})
    style.set_properties(fill_color = "#ffffcc")

    para = odf_create_paragraph(u"")
    body.append(para)

    # some computation of oordinates
    center, vlist = make_coords(side=12.0, vpos=8.0)

    # create a circle
    rad = 8.0
    pos = center - complex(rad, rad)
    circle = odf_create_ellipse(
        size=('%.2fcm' % (rad * 2), '%.2fcm' % (rad * 2) ),
        position=('%.2fcm' % pos.real, '%.2fcm' % pos.imag) )
    para.append(circle)

    # create a drawing with a lot of lines
    para.append(u'number of lines: %s' % len(vlist))
    for v in vlist:
        line = odf_create_line(p1 = v.in_cm(0), p2 = v.in_cm(1))
        para.append(line)

if not os.path.exists('test_output'):
    os.mkdir('test_output')

output = os.path.join('test_output', 'my_Koch_fractal.odt')

document.save(target=output, pretty=True)
