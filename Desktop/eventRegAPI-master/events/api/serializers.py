from rest_framework import serializers
from events.models import Event, EventRegistration

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        exclude = ['id']


class EventRegistrationSerializer(serializers.ModelSerializer):
    # event = serializers.StringRelatedField()
    # user = serializers.StringRelatedField()

    class Meta:
        model = EventRegistration
        exclude = ['id']
