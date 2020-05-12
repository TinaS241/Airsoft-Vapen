from django.shortcuts import render


from django.shortcuts import render 
from .models import Airsoft

def upload_image(request):
    my_image = request.FILES['my_image']
    model = MyModel(..., my_image=my_image)
    model.save()