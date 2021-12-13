from django.db import models

# Create your models here.

# create a model contact model with three fields
class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.name
