from django.db import models
from tinymce.models import HTMLField

class Test(models.Model):
    objects = models.Manager()
    content = HTMLField()
