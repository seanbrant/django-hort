import math


def make_iterable(*args):
    """
    Takes args passed in and returns a iterable of the args. If
    args is a list or tuple it flattens the values.

    """
    for arg in args:
        if isinstance(arg, (list, tuple)):
            for a in arg:
                yield a
        else:
            yield arg


def section(iterable, by):
    x = int(math.ceil(float(len(iterable)) / float(by)))
    for i in xrange(x):
        yield iterable[by * i:by * (i + 1)]


def chunk(iterable, by):
    x = int(math.ceil(float(len(iterable)) / float(by)))
    for i in xrange(x):
        r = iterable[x * i:x * (i + 1)]
        if r:
            yield r
