from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("caisse/", include("caisse.urls")),
    # la racine redirige vers /caisse/dashboard/ sans importer la vue directement
    path("", RedirectView.as_view(url="/caisse/dashboard/", permanent=False), name="home"),
]


