import itertools

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from templatetag_sugar.parser import Constant, Name, Optional, Variable
from templatetag_sugar.register import tag

from hort.utils import iterators


register = template.Library()


@tag(register, (
    Variable(),
    Constant('by'),
    Variable(),
    Constant('as'),
    Name(),
))
def chunk(context, iterable, n, asvar):
    context[asvar] = iterators.chunk(iterable, n)
    return ''


@tag(register, (
    Variable(),
    Constant('by'),
    Variable(),
    Constant('as'),
    Name(),
))
def section(context, iterable, n, asvar):
    context[asvar] = iterators.section(iterable, n)
    return ''


@tag(register, (
    Variable(),
    Constant('as'),
    Name(),
))
