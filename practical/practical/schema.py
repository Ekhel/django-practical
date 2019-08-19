import graphene
from editor.schema import Query as snippet_query

class Query(snippet_query):
    pass

schema = graphene.Schema(query=Query)