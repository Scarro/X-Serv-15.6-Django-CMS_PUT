from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pages(models.Model):
    nombre = models.CharField(max_length=200)
    recurso = models.TextField()

    def __str__(self):
        return self.recurso
