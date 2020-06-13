from django import forms
from .models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')





class UserLoginForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-box', 'title': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'user_login form-control text-box'}))

    class Meta:
        model = User
        fields = ('email', 'password')

class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'driving_license_no',
            'password'
        ]