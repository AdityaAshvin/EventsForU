from django.db import models
import uuid

# Create your models here

class Contact(models.Model):
    name= models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    phone= models.CharField(max_length=122)
    desc= models.TextField()

    def __str__(self):
        return self.name

class EventPage(models.Model):
    id = models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False) 
    title= models.CharField(max_length=122)
    header= models.CharField(max_length=122)
    desc= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    location= models.TextField(default='')
    tag= models.CharField(max_length=122, default='')
    organizer= models.CharField(max_length=122, default='')

    def __str__(self):
        return self.title
    

