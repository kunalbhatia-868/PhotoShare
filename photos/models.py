from django.db import models
from django.db.models.base import Model

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    description=models.TextField()
    image=models.ImageField(blank=False,null=False)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.description