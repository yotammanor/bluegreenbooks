# copied and adapted from:
# https://github.com/jazzband/django-hosts/
# blob/master/django_hosts/middleware.py

from django.conf import settings
from django.urls import (
    get_urlconf,
    set_urlconf,
)

from .switch import get_color


class ColorRouterBaseMiddleware:
    """
    Adjust incoming request's urlconf based on hosts defined in
    settings.ROOT_HOSTCONF module.
    """

    def __init__(self, get_response=None):
        self.get_response = get_response
        self.current_urlconf = None

    def get_urlconf_by_color(self):
        if not hasattr(settings, "MIGRATION_NAME_SWITCH"):
            return settings.ROOT_URLCONF
        color = get_color(migration_name=settings.MIGRATION_NAME_SWITCH)
        return f'router.urls.{color}'


class ColorRouterRequestMiddleware(ColorRouterBaseMiddleware):
    def __call__(self, request):
        url_conf = self.get_urlconf_by_color()
        # This is the main part of this middleware
        request.urlconf = url_conf
        # But we have to temporarily override the URLconf
        # already to allow correctly reversing url_Conf URLs in
        # the url_Conf callback, if needed.
        current_urlconf = get_urlconf()
        try:
            set_urlconf(url_conf)
        finally:
            # Reset URLconf for this thread on the way out for complete
            # isolation of request.urlconf
            set_urlconf(current_urlconf)
        return self.get_response(request)


class ColorRouterResponseMiddleware(ColorRouterBaseMiddleware):
    def __call__(self, request):
        response = self.get_response(request)
        url_conf = self.get_urlconf_by_color()
        request.urlconf = url_conf
        set_urlconf(url_conf)
        return response
