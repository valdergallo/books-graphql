from __future__ import absolute_import
from graphene_django import DjangoObjectType
import graphene
from books.schemas.nodes import BookNode
from books.models import Book
from haystack.query import SearchQuerySet


class Query(graphene.ObjectType):
    books = graphene.List(BookNode)

    @graphene.resolve_only_args
    def resolve_books(self):
        # return Book.objects.all()
        result = SearchQuerySet().filter(content='book').order_by('-pub_date')
        return result



books_schema = graphene.Schema(query=Query)