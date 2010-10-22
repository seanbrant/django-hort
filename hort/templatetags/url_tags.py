from django import template
from django.template.defaulttags import kwarg_re

register = template.Library()


class LazyURLNode(template.Node):

    def __init__(self, reverse, args, kwargs, asvar):
        self.reverse = reverse
        self.args = args
        self.kwargs = kwargs
        self.asvar = asvar

    def render(self, context):
        reverse = self.reverse.resolve(context)
        args = [arg.resolve(context) for arg in self.args]
        kwargs = dict((smart_str(k, 'ascii'), v.resolve(context))
            for k, v in self.kwargs.iteritems())
        url = reverse.reverse(*args, **kwargs)
        if self.asvar:
            context[self.asvar] = url
            return ''
        else:
            return url


@register.tag
def lazyreverse(parser, token):
    bits = token.split_contents()
    if len(bits) < 2:
        raise template.TemplateSyntaxError("'%s' takes at least one argument"
                                           " (lazy reverse object)" % bits[0])
    reverse = parser.compile_filter(bits[1])
    args = []
    kwargs = {}
    asvar = None
    bits = bits[2:]
    if len(bits) >= 2 and bits[-2] == 'as':
        asvar = bits[-1]
        bits = bits[:-2]

    if len(bits):
        for bit in bits:
            match = kwarg_re.match(bit)
            if not match:
                raise template.TemplaetSyntaxError("Malformed arguments to url tag")
            name, value = match.groups()
            if name:
                kwargs[name] = parser.compile_filter(value)
            else:
                args.append(parser.compile_filter(value))

    return LazyURLNode(reverse, args, kwargs, asvar)
