from django.urls import path
from . import views

urlpatterns = [
    path("suivi/", views.suivi_caisse, name="suivi_caisse"),
    path("recap/", views.recap_mensuel, name="recap_mensuel"),
    path("dashboard/", views.dashboard, name="dashboard"),

    path("export-excel/", views.export_excel, name="export_excel"),
    path("export-pdf/", views.export_pdf, name="export_pdf"),

    path("mouvement/nouveau/", views.mouvement_create, name="mouvement_create"),

    path("api/mensuel/", views.api_mensuel, name="api_mensuel"),
]






