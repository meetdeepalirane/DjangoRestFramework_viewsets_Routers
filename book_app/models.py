from django.db import models

# Create your models here.


class Book(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    price=models.IntegerField()

    def __str__(self):
        return '%s %s %s' %(self.name,self.author,self.price)

