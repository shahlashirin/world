from django.db import models

# Create your models here.
class blog(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to="image")
