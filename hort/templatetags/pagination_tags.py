from django import template
from django.conf import settings

register = template.Library()


PAGINATION_RANGE = getattr(settings, 'PAGINATION_RANGE', 20)
PAGINATION_TRAILING = getattr(settings, 'PAGINATION_TRAILING', 2)


@register.inclusion_tag('hort/pagination.html', takes_context=True)
def pagination(context, object_list_view,
        pagination_range=PAGINATION_RANGE,
        pagination_trailing=PAGINATION_TRAILING):
    page_obj = context['page_obj']
    paginator = context['paginator']
    pages = paginator.num_pages
    page = page_obj.number
    adjacent_pages = pagination_trailing * 2
    inside_range = pagination_range - pagination_trailing

    if not page_obj.has_other_pages():
        return {}

    pages_before = pages_after = range(0)

    if pages <= pagination_range:
        page_range = [n for n in range(1, pages + 1) if n > 0 and n <= pages]
    elif page <= inside_range:
        page_range = [n for n in range(1, pagination_range + 1) if n > 0 and n <= pages]
        pages_after = [n + context["pages"] for n in range(0, -pagination_trailing, -1)]
    elif page > pages - inside_range:
        page_range = [n for n in range(pages - pagination_range + 1, pages + 1) if n > 0 and n <= pages]
        pages_before = [n + 1 for n in range(0, pagination_trailing)]
    else:
        page_range = [n for n in range(page - adjacent_pages, page + adjacent_pages + 1) if n > 0 and n <= pages]
        pages_after = [n + context["pages"] for n in range(0, -pagination_trailing, -1)]
        pages_before = [n + 1 for n in range(0, pagination_trailing)]

    return {
        'object_list_view': object_list_view,
        'page_obj': page_obj,
        'paginator': paginator,
        'page_range': page_range,
        'pages_before': pages_before,
        'pages_after': pages_after,
    }
