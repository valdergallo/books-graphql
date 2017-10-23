from __future__ import absolute_import
from django.db import models
from core.models import Tags
from authors.models import Author


class Book(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tags)
    points = models.IntegerField()
    pub_date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.name


class BestSellers(models.Model):
    year = models.DateField()
    book = models.ForeignKey(Book)
    author = models.ForeignKey(Author, related_name='best_sellers')