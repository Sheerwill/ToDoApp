from django.urls import path, include
from .views import CustomLoginView, home #delete_todo
from rest_framework import routers
from .views import ToDoModelViewSet
from . models import ToDoModel

router = routers.DefaultRouter(trailing_slash = False)
router.register(r'ToDoModel', ToDoModelViewSet)

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('home/', home, name = 'home'),
    #path('home/<int:todo_id>/', delete_todo, name='delete_todo'),
    path('home/api/', include(router.urls)),
]
