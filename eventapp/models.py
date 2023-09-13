from django.db import models

# Create your models here.
class Event(models.Model):  #inheriting models
    event_title=models.CharField(max_length=120)
    location=models.CharField(max_length=70)
    date=models.CharField(max_length=120)
    description=models.TextField()
    def __str__(self):
        return self.event_title

class Detail(models.Model):  #inheriting models
    fullname=models.CharField(max_length=120)
    email=models.EmailField(max_length=254)
    phone=models.IntegerField()
    event=models.ForeignKey('Event',on_delete=models.CASCADE)
    def __str__(self):
        return self.fullname