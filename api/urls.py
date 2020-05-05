from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AirsoftExternalViewSet, AirsoftInternalViewSet, CommentViewSet

router = DefaultRouter()

router.register('AirsoftExternal', AirsoftExternalViewSet, basename='AirsoftExternal')
router.register('AirsoftInternal', AirsoftInternalViewSet, basename='AirsoftInternal')
router.register('Comment', CommentViewSet, basename='Comment')



# urlpatterns = router.urls

urlpatterns = [
    path('',include(router.urls)),
]



