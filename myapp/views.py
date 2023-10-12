from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .forms import ToDoForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')

@login_required
def home(request):        
    if request.method == 'GET':
        form = ToDoForm()
        return render(request, 'home.html', {"form": form})
    else:
        form = ToDoForm(request.POST)
        if form.is_valid():
            new_todo = form.save(commit=False)  
            new_todo.user = request.user  
            new_todo.save()

            return HttpResponse('Fine')
        else:
            raise Http404('Bad request')