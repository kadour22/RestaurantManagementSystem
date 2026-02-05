from django.db import models

class Restaurant(models.Model) :
    name = models.CharField(max_length=150, unique=True)
    logo = models.ImageField(upload_to='logos')
    adresse = models.CharField(max_length=200)

    def __str__(self) :
        return self.name
    