from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .forms import ToDoForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import ToDoModel
from django.http import JsonResponse
from rest_framework import viewsets, filters
from .serializers import ToDoModelSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')

@login_required
def home(request):
    '''if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            new_todo = form.save(commit=False)
            new_todo.user = request.user  # Associate the to-do with the logged-in user
            new_todo.save()
            return HttpResponse(status=201)
        else:
            raise Http404('Bad request')    
        
    else:'''
    form = ToDoForm()    
    todo_items = ToDoModel.objects.filter(user=request.user).order_by('-id') 
    return render(request, 'home.html', {"form": form, "todo_items": todo_items})

'''@login_required
def delete_todo(request, todo_id):
    try:
        todo_item = ToDoModel.objects.get(id=todo_id, user=request.user)
        todo_item.delete()
        return JsonResponse({"message": "Todo item deleted successfully."}, status=200)
    except ToDoModel.DoesNotExist:
        return JsonResponse({"error": "Todo item not found."}, status=404)
    except Exception as e:
        return JsonResponse({"error": "An error occurred while deleting the todo item."}, status=500)'''

class ToDoModelViewSet(viewsets.ModelViewSet):
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'user', 'entry']
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Set the user field of the model to the currently logged-in user
        serializer.save(user=self.request.user)

        