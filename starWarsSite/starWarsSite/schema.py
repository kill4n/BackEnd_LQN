import graphene

from graphene import relay
import starWarsSite.starWarsApp.schema
from starWarsSite.starWarsApp.schema import PersonajeMutation, PlanetaMutation, PeliculaMutation

class Query(starWarsSite.starWarsApp.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class MyMutations(graphene.ObjectType):
    create_personaje = PersonajeMutation.Field()
    create_planeta = PlanetaMutation.Field()
    create_pelicula = PeliculaMutation.Field()

schema = graphene.Schema(query=Query, mutation=MyMutations)
