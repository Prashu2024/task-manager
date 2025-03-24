from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User
from .serializers import UserSerializer, UserCreateSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer
