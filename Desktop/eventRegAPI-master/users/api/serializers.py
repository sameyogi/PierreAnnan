from rest_framework import serializers
from django.contrib.auth.models import User
from events.api.serializers import EventRegistrationSerializer

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'events']
