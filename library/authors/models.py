from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    birth_date = models.DateField(null=True)

    def get_full_name(self):
        return self.first_name + self.last_name

    def __str__(self):
        return self.get_full_name()


class AuthorBio(models.Model):
    author = models.ForeignKey(Author)
    text = models.TextField()

    def __str__(self):
        return self.text


class AuthorPostMsg(models.Model):
    author = models.ForeignKey(Author)
    link = models.SlugField()
    title = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.text
