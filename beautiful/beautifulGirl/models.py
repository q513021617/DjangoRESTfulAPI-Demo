from django.db import models

from django.contrib.auth.models import User


class Beautiful(models.Model):
    GirlName = models.CharField(max_length=20)
    ImageUrl = models.CharField(max_length=200)

    def __str__(self):
        return str(self.GirlName)
