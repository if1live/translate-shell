#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
tk calculate
from https://translate.google.com/translate/releases/twsfe_w_20151214_RC03/r/js/desktop_module_main.js
translate.google.com/desktop_module_main.js (formatted) : 8117
function name : TL
"""

import sys
import ctypes
import logging
import time

#logging.basicConfig(level=logging.DEBUG)

text = u" ".join(sys.argv[1:])
byte_array = [int(x) for x in list(text.encode("utf-8"))]

def RL(a, b):
    logging.debug("initial  a: {}".format(a))
    for c in range(0, len(b) - 2, 3):
        t = ord('a')
        Tb = ord("+")

        d = b[c + 2]

        if ord(d) >= t:
            d = ord(d) - 87
        else:
            d = int(d)
        logging.debug("first a: {}, d: {}".format(a, d))

        if ord(b[c + 1]) == Tb:
            xa = ctypes.c_uint32(a)
            d = xa.value >> d

        else:
            xa = ctypes.c_uint32(a)
            d = xa.value << d

        logging.debug("before a: {}, d: {}".format(a, d))

        if ord(b[c]) == Tb:
            xa, xd, xc = ctypes.c_int32(a), ctypes.c_int32(d), ctypes.c_int32(4294967295)
            a = xa.value + xd.value & xc.value

        else:
            a = a ^ d
        logging.debug("after a: {}".format(a))

    logging.debug("final a: {}\n\n".format(a))
    return a

SL = int(time.time() / 3600)
b = SL

d = byte_array
a = b
Vb = "+-a^+6"
Ub = "+-3^+b+-f"

for e in range(0, len(d)):
    a += d[e]
    logging.debug("step {} : a={}".format(e, a))
    a = RL(a, Vb)

a = RL(a, Ub)
if 0 > a:
    a = (a & 2147483647) + 2147483648
a = int(a % 1E6)

tk="{}.{}".format(a, a ^ b)
print(tk)
