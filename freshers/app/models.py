from django.db import models

# Create your models here.
class Confession(models.Model):
    name=models.TextField(max_length=200)
    subject=models.TextField()
    def __str__(self):
        return self.name