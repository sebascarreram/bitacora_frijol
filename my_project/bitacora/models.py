from django.db import models


# Create your models here.
class Etapas(models.Model):
    id_etapa = models.AutoField(primary_key=True)
    id_planta = models.ForeignKey("Plantas", models.DO_NOTHING, db_column="id_planta")
    nombre_etapa = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    edad_planta = models.IntegerField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_etapa}"


class Experimentos(models.Model):
    id_experimento = models.AutoField(primary_key=True)
    id_planta = models.ForeignKey("Plantas", models.DO_NOTHING, db_column="id_planta")
    id_usuario = models.ForeignKey(
        "Usuarios", models.DO_NOTHING, db_column="id_usuario"
    )
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.id_experimento} - {self.descripcion}"


class Plantas(models.Model):
    id_planta = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(
        "Usuarios", models.DO_NOTHING, db_column="id_usuario"
    )
    nombre_comun = models.CharField(max_length=100)
    nombre_cientifico = models.CharField(max_length=150, blank=True, null=True)
    familia = models.CharField(max_length=100, blank=True, null=True)
    region_origen = models.CharField(max_length=100, blank=True, null=True)
    rareza = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.familia} - {self.region_origen}"


class Registros(models.Model):
    id_registro = models.AutoField(primary_key=True)
    id_planta = models.ForeignKey(Plantas, models.DO_NOTHING, db_column="id_planta")
    altura_cm = models.FloatField(blank=True, null=True)
    hojas = models.IntegerField(blank=True, null=True)
    luz_horas = models.FloatField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.id_registro} - {self.id_planta}"


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=100)
    correo_electronico = models.CharField(unique=True, max_length=100)
    contrasena_usuario = models.CharField(max_length=255)
    edad = models.IntegerField(blank=True, null=True)
    telefono_celular = models.CharField(max_length=20, blank=True, null=True)
    rol = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_usuario}"
