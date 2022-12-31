from django import forms
from django.forms import ModelForm
from .models import CarInfo, Customer


class RentCarForm(forms.ModelForm):
    class Meta:
        model = CarInfo
        fields = ['car_brand', 'car_model', 'type', 'size']
        
class UploadForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        

    #     first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # email = models.EmailField(unique=True)
    # phone_number = models.IntegerField()
    # address = models.CharField(max_length=200)
    # city = models.CharField(max_length=100)
    # country = mo