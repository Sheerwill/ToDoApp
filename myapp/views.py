from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .forms import ToDoForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import ToDoModel

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')

@login_required
def home(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            new_todo = form.save(commit=False)
            new_todo.user = request.user  # Associate the to-do with the logged-in user
            new_todo.save()
            return HttpResponse(status=201)
        else:
            raise Http404('Bad request')
    else:
        form = ToDoForm()
    # Retrieve to-do items for the current user from the database
    todo_items = ToDoModel.objects.filter(user=request.user)
    return render(request, 'home.html', {"form": form, "todo_items": todo_items})
        