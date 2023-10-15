from rest_framework import serializers
from .models import ToDoModel

class ToDoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoModel
        fields = ['id', 'entry']
