from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
