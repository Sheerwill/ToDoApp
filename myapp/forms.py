from django import forms
from . models import ToDoModel
from django.forms.widgets import SelectDateWidget

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoModel
        fields = ["entry", "date", "time"]    