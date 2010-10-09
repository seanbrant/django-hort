=========
Shortcuts
=========


``render``
==========

.. function:: render(template_name, [request, dictionary=None, content_type=None, status=None, template_loader=loader,
context_processors=None])

    Renders a given template with a given context dictionary and returns an
    :class:`~django.http.HttpResponse` object with that rendered text.

Required arguments
------------------

``template_name``
    The full name of a template to use or a iterable of template names.

Optional arguments
------------------

``request``

    A :class:`~django.http.HttpRequest` object. If this is passed a :class:`RequestContext`
    is automatically used rather then the default :class:`Context`.

``context``

    A dictionary of values to add to the template context. By default, this
    is an empty dictionary. If a value in the dictionary is callable, the
    view will call it just before rendering the template.

``content_type``

    The Content-Type to use for the resulting document. Defaults to the value or
    the ``DEFAULT_CONTENT_TYPE`` setting.

``status``

    The Http status to use for the resulting document. Defaults to 200.

``template_loader``

    The ``template_loader`` to use when loading the passed in ``template_name``. Defaults
    to ``django.template.loader``.

``context_processors``

    List if template context processors. Defaults to the ``TEMPLATE_CONTEXT_PROCESSORS`` setting.
