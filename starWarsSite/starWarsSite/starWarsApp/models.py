from django.db import models

# Modelo de los Personajes


class Personaje(models.Model):
    nombre = models.CharField(max_length=120)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre

# Modelo de los Planetas


class Planeta(models.Model):
    nombre = models.CharField(max_length=120)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre

# Modelo de las Películas


class Pelicula(models.Model):
    titulo = models.CharField(max_length=120)
    texto_apertura = models.TextField()
    director = models.CharField(max_length=120)
    productores = models.CharField(max_length=120)
    personaje = models.ManyToManyField(Personaje)
    planeta = models.ManyToManyField(Planeta)

    class Meta:
        ordering = ('titulo',)

    def __str__(self):
        return self.titulo
