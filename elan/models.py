from django.db import models

# Create your models here.
class Elan (models.Model):
    elanTitle = models.CharField(max_length=200)
    elanDescription = models.CharField(max_length=200)
    elanPrice = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    ownerPhone = models.CharField(max_length=200)
    ownerMail = models.CharField(max_length=200, blank=True)
    itemCategory = models.CharField(max_length=200)
    image = models.FileField(null=True, blank=True)


    def __str__(self):
        return self.elanTitle

