from django.db import models
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect
from django.utils.html import mark_safe


class Carta(models.Model):
    id_carta = models.PositiveIntegerField(db_index=True)
    nombre = models.CharField(max_length=200)
    
    class tipoArcano(models.TextChoices):
        MAYOR = "MA", _("Mayor")
        MENOR = "ME", _("Menor")

    arcano = models.CharField(
        max_length=5,
        choices=tipoArcano.choices,
        default=tipoArcano.MAYOR,
        )

    mazo = models.CharField(max_length=200)     
    pinta = models.CharField(max_length=50)
    numero = models.IntegerField()
    descripcion = models.TextField()
    publicado = models.DateTimeField(blank=True, null=True)
    imagen = models.ImageField()

    def __str__(self):
        return f"{self.numero} - {self.nombre}"
    
    class Meta:
        ordering = ['numero']
 