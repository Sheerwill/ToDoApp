from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpResponse

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')

def home(request):
    if request.method == 'GET':
        return HttpResponse("Success!")
