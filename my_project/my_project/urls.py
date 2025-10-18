"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from bitacora.views import (
    Index,
    RegistrarEstudiante,
    RegistrarMedicion,
    RegistroFotografico,
    TablaMediciones,
    GraficaRegresion,
    ExportarCSV,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Index.as_view(), name="index"),
    path(
        "registrar_estudiante/",
        RegistrarEstudiante.as_view(),
        name="registrar_estudiante",
    ),
    path("registrar_medicion/", RegistrarMedicion.as_view(), name="registrar_medicion"),
    path(
        "registro_fotografico/",
        RegistroFotografico.as_view(),
        name="registro_fotografico",
    ),
    path("tabla_mediciones/", TablaMediciones.as_view(), name="tabla_mediciones"),
    path("grafica_regresion/", GraficaRegresion.as_view(), name="grafica_regresion"),
    path("exportar_csv/", ExportarCSV.as_view(), name="exportar_csv"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
