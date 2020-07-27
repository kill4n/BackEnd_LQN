import graphene

from graphene import relay, ObjectType, Mutation
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from starWarsSite.starWarsApp.models import Planeta, Personaje, Pelicula


class PersonajeNode(DjangoObjectType):
    class Meta:
        model = Personaje
        filter_fields = {
            'nombre': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )

class PlanetaNode(DjangoObjectType):
    class Meta:
        model = Planeta
        filter_fields = {
            'nombre': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )

class PeliculaNode(DjangoObjectType):
    class Meta:
        model = Pelicula
        # Allow for some more advanced filtering here
        filter_fields = {
            'titulo': ['exact', 'icontains', 'istartswith'],
            'texto_apertura': ['exact', 'icontains'],
            'director': ['exact'],
            'productores': ['exact'],
            'personaje': ['exact'],
            'personaje__nombre': ['exact'],
            'planeta': ['exact'],
            'planeta__nombre': ['exact'],
        }
        interfaces = (relay.Node,)

class PersonajeMutation(Mutation):
    class Arguments:
        nombre = graphene.String(required = True)
        id = graphene.ID()

    personaje = graphene.Field(PersonajeNode)

    def mutate(self, info, nombre, id):
        personaje = Personaje.objects.get(pk=id)
        personaje.nombre = nombre
        personaje.save()

        return PersonajeMutation(personaje=personaje)

class PlanetaMutation(Mutation):
    class Arguments:
        nombre = graphene.String(required = True)
        id = graphene.ID()

    planeta = graphene.Field(PlanetaNode)

    def mutate(self, info, nombre, id):
        planeta = Planeta.objects.get(pk=id)
        planeta.nombre = nombre
        planeta.save()

        return PlanetaMutation(planeta=planeta)

class PeliculaMutation(Mutation):
    class Arguments:
        titulo = graphene.String(required = True)
        texto_apertura = graphene.String(required = True)
        director = graphene.String(required = True)
        productores = graphene.String(required = True)
        id = graphene.ID()

    pelicula = graphene.Field(PeliculaNode)

    def mutate(self, info, titulo, texto_apertura, director, productores, id):
        pelicula = Pelicula.objects.get(pk=id)
        pelicula.titulo = titulo
        pelicula.texto_apertura = texto_apertura
        pelicula.director = director 
        pelicula.productores = productores
        pelicula.save()

        return PeliculaMutation(pelicula=pelicula)

class Mutation(ObjectType):
    update_personaje = PersonajeMutation.Field()
    update_planeta = PlanetaMutation.Field()
    update_pelicula = PeliculaMutation.Field()

class Query(graphene.ObjectType):
    personaje = relay.Node.Field(PersonajeNode)
    all_personajes = DjangoFilterConnectionField(PersonajeNode)

    pelicula = relay.Node.Field(PeliculaNode)
    all_peliculas = DjangoFilterConnectionField(PeliculaNode)

    planeta = relay.Node.Field(PlanetaNode)
    all_planetas = DjangoFilterConnectionField(PlanetaNode)
