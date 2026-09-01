from django.db import models

# Create your models here.
class Detail(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    password=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)

    def __str__(self):
        return self.name