#!/usr/bin/env python
# -*- coding: utf-8 -*-

def _encode(loc, scale):
    val = 0
    if loc < 0:
        val = 1000000000
    else:
        val = 2000000000
    val += loc * scale
    if val > 3000000000:
        raise OverflowError
    val = hex(int(val))[2:]
    first = unichr(int(val[:4], 16))
    second = unichr(int(val[4:], 16))
    return first, second

def encode(lon, lat):
    ''' encode takes a longitude and a latitude and using the algorithm
    described in the README(Todo) creates a 4 character unicode string '''
    first, second = _encode(lat, 10000000)
    third, fourth = _encode(lon, 1000000)
    return first, second, third, fourth

def decode(code):
    pass
