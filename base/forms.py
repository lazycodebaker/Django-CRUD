
from django import forms
from .models import User

class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','age','email','number','password']

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'age' : forms.NumberInput(attrs={'class':'form-control'}),
            'number' : forms.NumberInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'})
        }



      

        
