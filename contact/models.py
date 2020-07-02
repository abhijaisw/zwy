from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=15)
    sub = models.CharField(max_length=100)
    desc = models.CharField(max_length=5000)

    def __str__(self):
        return self.name