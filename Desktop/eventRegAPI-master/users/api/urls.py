from django.urls import path, re_path
from .views import UserDetailAPIView

app_name = 'users'

urlpatterns = [
    path('users/<int:id>', UserDetailAPIView.as_view(), name='user-list'),
]