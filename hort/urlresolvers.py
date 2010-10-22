from django.core.urlresolvers import reverse


class LazyReverse(object):

    def __init__(self, viewname, urlconf=None, args=None,
            kwargs=None, prefix=None, current_app=None):
        self.viewname = viewname
        self.urlconf = urlconf
        self.args = args or []
        self.kwargs = kwargs or {}
        self.prefix = prefix
        self.current_app = current_app

    def reverse(self, *extra_args, **extra_kwargs):
        args = []
        args.extend(self.args)
        args.extend(extra_args)
        kwargs = {}
        kwargs.update(self.kwargs)
        kwargs.update(extra_kwargs)
        return reverse(self.viewname, self.urlconf, args,
            kwargs, self.prefix, self.current_app)
