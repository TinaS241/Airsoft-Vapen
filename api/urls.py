from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import AirsoftExternalViewSet, AirsoftInternalViewSet, CommentViewSet

router = SimpleRouter()

router.register('', AirsoftExternalViewSet, basename='AirsoftExternal')
router.register('', AirsoftInternalViewSet, basename='AirsoftInternal')
router.register('', CommentViewSet, basename='Comment')



urlpatterns = router.urls