from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView


urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
    path(settings.ADMIN_URL, admin.site.urls),

    path("users/", include("tarot.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
   
    #PRUEBA CON TIRADA
    #path("tirada/", TemplateView.as_view(template_name="pages/tirada.html"), name="tirada"),
    path("", include("tarot.carta.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
   urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Malo tu pedido")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("No hay permiso para ver esta página")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Página no existe, búscala en el")},
        ),
        path("500/", default_views.server_error),
    ]
if "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
