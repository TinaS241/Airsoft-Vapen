from django.shortcuts import render

# from .forms import model_type

# def home_view(request):
#     context = {}
#     content['form'] =  ModelForm()
#     return render(request, "newgun.html", context)



from django.shortcuts import render 
from .forms import GeeksForm 

# Create your views here. 
def home_view(request): 
	context = {} 
	context['form'] = GeeksForm() 
	return render( request, "home.html", context) 
