from django.db import models


class Tags(models.Model):
    tag = models.SlugField(db_index=True, unique=True)

    def __str__(self):
        return self.tag