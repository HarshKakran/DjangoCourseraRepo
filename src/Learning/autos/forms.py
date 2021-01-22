from django.forms import ModelForm
from .models import Auto

class MakeForm(ModelForm):
    class Meta:
        model = Auto
        fields= '__all__'