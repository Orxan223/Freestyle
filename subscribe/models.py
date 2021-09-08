from django.db import models

# Create your models here.


class Anons(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(null=True, blank=True)

   

    class Meta:
        verbose_name_plural = 'Anons'


class Subscribe(models.Model):
    email = models.EmailField(null=True, blank=True,unique=True)

