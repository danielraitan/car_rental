from django import forms
from django.forms import ModelForm
from .models import CarInfo, Customer


class RentCarForm(forms.ModelForm):
    class Meta:
        model = CarInfo
        fields = '__all__'
        
class UploadForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        