from django.urls import path
from .views import CustomLoginView, home

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('home/', home, name = 'home')
]