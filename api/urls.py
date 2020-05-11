from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AirsoftViewSet,CommentViewSet,UserViewSet

router = DefaultRouter()

router.register('Airsoft', AirsoftViewSet, basename='Airsoft')
router.register('Comment', CommentViewSet, basename='Comment')
router.register('User', UserViewSet, basename='User')
# router.register('ModelViewSet', ModelViewSet, basename='ModelList')



urlpatterns = [
    path('',include(router.urls)),
]



