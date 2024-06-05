from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150)

    def __str__(self):
        return str(self.username)
