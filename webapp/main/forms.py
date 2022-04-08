from .models import Webapp
from django.forms import ModelForm, TextInput


class WebappForm(ModelForm):
    class Meta:
        model = Webapp
        fields = ["login" , "password"]
        widgets = {
            "login": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин'}),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'}), }
