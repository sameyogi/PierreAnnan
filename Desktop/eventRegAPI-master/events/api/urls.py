from django.urls import path, re_path
from .views import EventListCreateAPIView, EventRegistrationCreateAPIView

app_name = 'events'

urlpatterns = [
    path('events', EventListCreateAPIView.as_view(), name='event-list'),
    path('registrations', EventRegistrationCreateAPIView.as_view(), name='registration'),
]