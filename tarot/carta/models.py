from django.db import models

class Carta(models.Model):
    id_carta = models.PositiveIntegerField(db_index=True)
    nombre = models.CharField(max_length=200)
    mazo = models.CharField(max_length=200)     
    arcano = models.TextChoices("Mayor", "Menor")
    pinta = models.CharField(max_length=50)
    numero = models.IntegerField()
    descripcion = models.TextField()
    publicado = models.DateTimeField(blank=True, null=True)
    imagen = models.ImageField()

    def __str__(self):
        return self.Carta