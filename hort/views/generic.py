from django.contrib import comments
from django.contrib.comments.views.comments import CommentPostBadRequest
from django.shortcuts import get_object_or_404
from django.template import loader

from hort.shortcuts import render


def object_detail_with_comments(request, queryset, object_id=None,
        slug=None, slug_field=None, extra_filters=None, template_name=None,
        template_name_field=None, template_loader=loader, extra_context=None,
        context_processors=None, template_object_name=None, content_type=None,
        comment_form_class=None, comment_model_class=None):

    slug_field = slug_field or 'slug'
    template_object_name = template_object_name or 'object'
    extra_context = extra_context or {}
    extra_filters = extra_filters or extra_filters

    model = queryset.model
    meta = model._meta

    if object_id:
        lookup = {'pk': object_id}
    elif slug and slug_field:
        lookup = {slug_field: slug}
    elif extra_filters is not None:
        lookup = {}
    else:
        raise AttributeError("Generic detail with comments must be called "
            "with object_id, slug/slug_field or extra_filters.")
    lookup.update(extra_filters)
    obj = get_object_or_404(queryset, **lookup)

    comment_form_class = comment_form_class or comments.get_form()
    comment_form_target = obj.get_absolute_url() or comments.get_form_target()
    if comment_model_class is None:
        comment_model_class = comments.get_model()

    comment_list = comment_model_class.objects.for_model(obj) \
        .select_related('user', 'user__profile')

    if not template_name:
        template_names = [
            '%s/%s_%s_detail.html' % (meta.app_label, obj.pk,
                meta.object_name.lower()),
            '%s/%s_detail.html' % (meta.app_label, meta.object_name.lower()),
        ]
    else:
        template_names = [template_name]
    if template_name_field:
        template_names.insert(0, getattr(obj, template_name_field))

    if request.method == 'POST':
        comment_form = comment_form_class(
            target_object=product,
            user=request.user,
            data=request.POST,
        )
        if comment_form.is_valid():
            comment, error = form.save(request)
            if error:
                return CommentPostBadRequest(error)
            return redirect('%s#comment-%s' % \
                (comment_form_target, comment.id))
    else:
        comment_form = comment_form_class(
            target_object=obj,
            user=request.user,
        )

    context = {
        template_object_name: obj,
        'comments': comment_list,
        'comment_form': comment_form,
        'comment_form_target': comment_form_target,
    }

    return render(
        template_name=template_names,
        request=request,
        context=context,
        content_type=content_type,
        template_loader=loader,
        context_processors=context_processors,
    )
