from tabnanny import verbose

from django.db import models

# Create your models here.


class Camaras(models.Model):
    ix = models.SmallIntegerField(primary_key=True, verbose_name="Canal")
    name = models.CharField(max_length=15, default="LIBRE", verbose_name="Nombre")
    desc = models.TextField(max_length=100, default="", verbose_name="Descripcion")
    show = models.BooleanField(default=True, verbose_name="Mostrar")

    def __str__(self):
        return f"{self.ix:2} - {self.name} - {self.desc[:20]}"

    class Meta:
        verbose_name = "Cámara"
        verbose_name_plural = "Cámaras"


class Umbrales(models.Model):
    ix = models.ForeignKey(Camaras, on_delete=models.CASCADE, related_name="Camaras_ix", verbose_name="Canal")
    low = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Límite inferior")
    high = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Límite superior")

    def __str__(self):
        return f"{self.ix} : {self.low} <=> {self.high}"

    class Meta:
        verbose_name = "Umbral"
        verbose_name_plural = "Umbrales"


class Registros(models.Model):
    ts = models.DateTimeField(primary_key=True, verbose_name="Fecha y hora")
    tipo = models.CharField(max_length=1, verbose_name="Tipo")
    ix = models.SmallIntegerField(verbose_name="Canal")
    temp = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Temperatura")

    class Meta:
        managed = False
        db_table = "vregistros"
