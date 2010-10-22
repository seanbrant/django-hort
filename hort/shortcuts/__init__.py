from django.http import HttpResponse
from django.template import Context, RequestContext
from django.template import loader

from hort.utils.iterators import make_iterable


def render(template_name, request=None, context=None,
        content_type=None, status=None, template_loader=loader,
        context_processors=None):
    if isinstance(template_name, (list, tuple)):
        template_names = make_iterable(template_name)
        template = template_loader.select_template(template_names)
    else:
        template = template_loader.get_template(template_name)

    context = context or {}
    for k, v in context.items():
        if callable(v):
            context[k] = v()
        else:
            context[k] = v

    if request:
        context_obj = RequestContext(request, context, context_processors)
    else:
        context_obj = Context(context)

    content = template.render(context_obj)
    return HttpResponse(content, content_type=content_type, status=status)
