from django.shortcuts import render, redirect
from django.views.generic.base import View
# from .models import Usuarios, RegistroFotografico, Registro, Planta
from .models import Usuarios


# Create your views here.

class Index(View):
    def get(self, request):
        return render(request, "index.html")
    
# 👩‍🎓 Registrar estudiante
class RegistrarEstudiante(View):
    def get(self, request):
        return render(request, "registrar_estudiante.html")

    def post(self, request):
        nombre = request.POST["nombre_usuario"]
        correo = request.POST["correo_electronico"]
        contrasena = request.POST["contrasena_usuario"]
        edad = request.POST.get("edad", None)
        telefono = request.POST.get("telefono_celular", "")
        rol = request.POST.get("rol", "Estudiante")

        Usuarios.objects.create(
            nombre_usuario=nombre,
            correo_electronico=correo,
            contrasena_usuario=contrasena,
            edad=edad if edad else None,
            telefono_celular=telefono,
            rol=rol
        )
        return redirect("index")

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
