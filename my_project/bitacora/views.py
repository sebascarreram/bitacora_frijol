from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.

class Index(View):
    def get(self, request):
        # return HttpResponse(content="Hola mundo desde django")
        data = {
            "name_application": "Aplicacion de prueba 1",
            "fecha_creacion": "Julio 28 de julio",
            "version": 1,
            "tecnologias": ["Python", "Django", "HTML", "CSS"],
        }
        return render(request, "index.html", context=data)
    
class RegistrarEstudiante(View):
    def get(self, request):
        return render(request, "registrar_estudiante.html")

class RegistrarMedicion(View):
    def get(self, request):
        return render(request, "registrar_medicion.html")

class RegistroFotografico(View):
    def get(self, request):
        return render(request, "registro_fotografico.html")

class TablaMediciones(View):
    def get(self, request):
        return render(request, "tabla_mediciones.html")

class GraficaRegresion(View):
    def get(self, request):
        return render(request, "grafica_regresion.html")

class ExportarCSV(View):
    def get(self, request):
        return render(request, "exportar_csv.html")
