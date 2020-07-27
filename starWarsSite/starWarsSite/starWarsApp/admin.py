from django.contrib import admin

# Register your models here.
from starWarsSite.starWarsApp.models import Planeta, Personaje, Pelicula

admin.site.register(Planeta)
admin.site.register(Personaje)
admin.site.register(Pelicula)