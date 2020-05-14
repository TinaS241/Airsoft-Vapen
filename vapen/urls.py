from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from . import views

from .views import upload_image

app_name = 'vapen'
urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),

    path('vapen/custom/', TemplateView.as_view(template_name="custom.html"), name='custom'),

    path('vapen/details/', TemplateView.as_view(template_name="details.html"), name='details'),

    path('vapen/riflepage/', TemplateView.as_view(template_name="riflepage.html"), name='riflepage'),
    path('vapen/riflepage/aegpistols/', TemplateView.as_view(template_name="aegpistols.html"), name='aegpistols'),
    path('vapen/riflepage/aegmachineguns/', TemplateView.as_view(template_name="aegmachineguns.html"), name='aegmachineguns'),
    path('vapen/riflepage/aegshotguns/', TemplateView.as_view(template_name="aegshotguns.html"), name='aegshotguns'),
    path('vapen/riflepage/aegsmg/', TemplateView.as_view(template_name="aegsmg.html"), name='aegsmg'),
    path('vapen/riflepage/newgun/', TemplateView.as_view(template_name="newgun.html"), name='newgun'),

    path('vapen/hpa/', TemplateView.as_view(template_name="hpa.html"), name='hpa'),
    path('vapen/hpa/hpapistols/', TemplateView.as_view(template_name="hpapistols.html"), name='hpapistols'),
    path('vapen/hpa/hpamachineguns/', TemplateView.as_view(template_name="hpamachineguns.html"), name='hpamachineguns'),
    path('vapen/hpa/hpashotguns/', TemplateView.as_view(template_name="hpashotguns.html"), name='hpashotguns'),
    path('vapen/hpa/hpasmg/', TemplateView.as_view(template_name="hpasmg.html"), name='hpasmg'),
    path('vapen/hpa/newgun/', TemplateView.as_view(template_name="newgun.html"), name='newgun'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)