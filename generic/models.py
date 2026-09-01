from django.db import models

# Create your models here.

class Yatri(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    email=models.EmailField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name