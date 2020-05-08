from django.shortcuts import render
from rest_framework import generics, viewsets


from vapen.models import Airsoft,Comment

from user.models import CustomUser

from .serializers import AirsoftSerializer
from .serializers import CommentSerializer
from .serializers import UserSerializer


class AirsoftViewSet(viewsets.ModelViewSet):
    queryset = Airsoft.objects.all()
    serializer_class = AirsoftSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


# def perform_create(self, serializer):
#     serializer.save(author=self.request.user)