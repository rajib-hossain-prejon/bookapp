from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Books(models.Model):
 name = models.CharField(max_length = 255)
 author = models.CharField(max_length = 255)