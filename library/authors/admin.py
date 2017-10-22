from django.contrib import admin
from authors.models import Author
from authors.models import AuthorBio
from authors.models import AuthorPostMsg

admin.site.register(Author)
admin.site.register(AuthorBio)
admin.site.register(AuthorPostMsg)