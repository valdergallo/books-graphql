from __future__ import absolute_import
from graphene_django import DjangoObjectType
import graphene
from books.models import Book


class BookNode(DjangoObjectType):
    class Meta:
        model = Book
        interfaces = (relay.Node,)
        # the same fields that are in search_indexes
        fields = ['name', 'description', 
        'author', 'tags', 'pub_date']
