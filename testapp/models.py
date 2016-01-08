from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

class UserList(models.Model):
    users = ArrayField(models.IntegerField(), default=[])

