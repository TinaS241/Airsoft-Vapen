from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404


from .models import CustomUser

from .forms import CustomUserCreationForm

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class UserProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'userprofile.html'

    def get_object(self):
        return get_object_or_404(CustomUser, username=self.kwargs['username'])