from django.db import models


class Perro(models.Model):

    TAMAÑOS = [
        ("Chico", "Chico"),
        ("Mediano", "Mediano"),
        ("Grande", "Grande"),
    ]

    ENERGIAS = [
        ("Poca", "Poca"),
        ("Media", "Media"),
        ("Mucha", "Mucha"),
    ]

    GENEROS = [
        ("Macho", "Macho"),
        ("Hembra", "Hembra"),
    ]

    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()
    tamaño = models.CharField(max_length=20, choices=TAMAÑOS)
    peso = models.FloatField()
    color = models.CharField(max_length=50)
    vacunado = models.BooleanField(default=False)
    adoptado = models.BooleanField(default=False)
    energia = models.CharField(max_length=20, choices=ENERGIAS)
    genero = models.CharField(max_length=20, choices=GENEROS)

    def __str__(self):
        return self.nombre
