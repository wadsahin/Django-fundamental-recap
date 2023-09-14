from django.db import models

# Create your models here.
class userModel(models.Model):
    uid = models.IntegerField()
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)