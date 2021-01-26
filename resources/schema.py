import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from database.models import Tech as TechModel


class Tech(MongoengineObjectType):

    class Meta:
        model = TechModel
        interfaces = (Node,)


class Query(graphene.ObjectType):
    node = Node.Field()
    all_movies = MongoengineConnectionField(Tech)


schema = graphene.Schema(types=[Tech], query=Query)
