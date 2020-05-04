from django.shortcuts import render
from rest_framework import generics, viewsets


from vapen.models import AirsoftExternal,AirsoftInternal,Comment

from .serializers import AirsoftInternalSerializer
from .serializers import AirsoftExternalSerializer
from .serializers import CommentSerializer


class AirsoftInternalViewSet(viewsets.ModelViewSet):
    queryset = AirsoftInternal.objects.all()
    serializer_class = AirsoftInternalSerializer


class AirsoftExternalViewSet(viewsets.ModelViewSet):
    queryset = AirsoftExternal.objects.all()
    serializer_class = AirsoftExternalSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

