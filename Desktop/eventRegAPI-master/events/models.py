from django.db import models
from django.contrib.auth.models import User

class Event (models.Model):
    time = models.CharField(max_length=20)
    speaker = models.CharField(max_length=100)
    topic = models.CharField(max_length=255)
    room_capacity = models.PositiveIntegerField()
    occupied = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'events' 

    def __str__(self):
        return f"{self.speaker} - {self.topic}"



class EventRegistration (models.Model):
    event = models.ForeignKey(Event, related_name='eventregistrations', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    #Metadata
    class Meta :
        verbose_name_plural = 'event Registrations'

    #Methods
    def __str__(self):
        return f"{self.event}"