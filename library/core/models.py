from django.db import models


class Tags(models.Model):
    tag = models.SlugField(db_index=True, unique=True)