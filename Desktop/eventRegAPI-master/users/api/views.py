from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserDetailAPIView(APIView):
    def get(self, request, id):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

