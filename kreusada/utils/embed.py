from random import randint as r

def random_colour():
    return "%06x" % r(0, 0xFFFFFF)