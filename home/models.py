from django.db import models

# Create your models here

class Contact(models.Model):
    name= models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    phone= models.CharField(max_length=122)
    desc= models.TextField()

    def __str__(self):
        return self.name

class Event(models.Model):
    title= models.CharField(max_length=122)
    header= models.CharField(max_length=122)
    desc= models.TextField()

    def __str__(self):
        return self.title
    

