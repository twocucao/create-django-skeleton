from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views import defaults as default_views
from django.views.generic import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)
redirect_api_all_view = RedirectView.as_view(url='/all', permanent=True)

urlpatterns = [
                  url(r'^', include('webapps.api.urls', namespace='api')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    import debug_toolbar

    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception("Bad Request!")}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception("Permission Denied")}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception("Page not Found")}),
        url(r'^500/$', default_views.server_error),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
