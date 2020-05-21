from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from rest_framework.decorators import api_view

from vapen.models import Airsoft,Comment

from user.models import CustomUser

from .serializers import AirsoftSerializer,CommentSerializer,UserSerializer

from .permissions import IsAuthorOrReadOnly



class AirsoftViewSet(viewsets.ModelViewSet):
    queryset = Airsoft.objects.all()
    serializer_class = AirsoftSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['modeltype']
    permission_classes = [IsAuthorOrReadOnly,IsAuthenticatedOrReadOnly]
    


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
    permission_classes = [IsAuthenticated,]

# class ApiViewSet(ApiView):
#     permission_classes = [IsAuthenticated,]



