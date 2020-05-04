from django.urls import path, include
from django.views.generic import TemplateView

from . import views

app_name = 'vapen'
urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('vapen/riflepage/', TemplateView.as_view(template_name="riflepage.html"), name='riflepage'),
    ]