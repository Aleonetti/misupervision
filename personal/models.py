from django.db import models

# Create your models here.
from django.db import models

class Escuela(models.Model):
    nombre = models.CharField("Nombre de la escuela", max_length=150)
    direccion = models.CharField("Dirección", max_length=200)
    localidad = models.CharField("Localidad", max_length=100)
    turno_manana = models.BooleanField("Turno mañana", default=True)
    turno_tarde = models.BooleanField("Turno tarde", default=False)
    cantidad_grados_manana = models.PositiveIntegerField("Cantidad de grados mañana", default=0)
    cantidad_grados_tarde = models.PositiveIntegerField("Cantidad de grados tarde", default=0)
    alumnos_manana = models.PositiveIntegerField("Cantidad de alumnos mañana", default=0)
    alumnos_tarde = models.PositiveIntegerField("Cantidad de alumnos tarde", default=0)
    cantidad_maestros = models.PositiveIntegerField("Cantidad de maestros", default=0)
    cantidad_directores = models.PositiveIntegerField("Cantidad de directores", default=0)
    tiene_gabinete = models.BooleanField("Gabinete profesional", default=False)
    tiene_porteros = models.BooleanField("Porteros", default=False)
    recibe_fondo_comedor = models.BooleanField("Recibe fondo para comedores", default=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Escuela"
        verbose_name_plural = "Escuelas"

class Maestro(models.Model):
    nombre = models.CharField("Nombre completo", max_length=100)
    dni = models.CharField("DNI", max_length=20, unique=True)
    escuela = models.ForeignKey(Escuela, verbose_name="Escuela", on_delete=models.CASCADE, related_name="maestros")
    alumnos_a_cargo = models.PositiveIntegerField("Cantidad de alumnos a cargo", default=0)
    cumple_ordenes = models.BooleanField("Cumple órdenes", default=True)
    fecha_ingreso = models.DateField("Fecha de ingreso")
    activo = models.BooleanField("Activo", default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Maestro/a"
        verbose_name_plural = "Maestros/as"

class Director(models.Model):
    nombre = models.CharField("Nombre completo", max_length=100)
    dni = models.CharField("DNI", max_length=20, unique=True)
    escuela = models.ForeignKey(Escuela, verbose_name="Escuela", on_delete=models.CASCADE, related_name="directores", null=True)
    fecha_ingreso = models.DateField("Fecha de ingreso")
    activo = models.BooleanField("Activo", default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directores"
