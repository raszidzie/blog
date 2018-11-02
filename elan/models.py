from django.db import models


# Create your models here.
class Elan (models.Model):
    user = models.ForeignKey('auth.User', related_name='elans')
    elanTitle = models.CharField(max_length=200)
    elanDescription = models.TextField()
    elanPrice = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    ownerPhone = models.CharField(max_length=200)
    ownerMail = models.CharField(max_length=200, blank=True)
    ownerCity = models.CharField(max_length=30)
    itemCategory = models.CharField(max_length=200)
    image = models.FileField(null=True, blank=True)


    def __str__(self):
        return self.elanTitle

    def get_absolute_url(self):
        return reverse('elanlar:elandetail', kwargs={'id': self.id})    

class ElanComment(models.Model):
    elan = models.ForeignKey('elan.Elan', related_name='comments', on_delete=models.CASCADE)
    name= models.CharField(max_length=200, verbose_name="Ad")
    comment = models.TextField(verbose_name="Yorum")
    date = models.DateTimeField(auto_now_add=True)

