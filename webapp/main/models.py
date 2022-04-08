from django.db import models

# Create your models here.

class Webapp(models.Model):
    login = models.CharField('Login',max_length=50)
    password = models.TextField('Password')

def __str__(self):
    return self.title

    class Meta:
        verbose_name = 'Логин'
        verbose_name_plural = 'Логины'