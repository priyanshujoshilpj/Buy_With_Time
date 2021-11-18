from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=128, required=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder': ('Username'), 'class': 'username'})

        self.fields['first_name'].widget.attrs.update(
            {'placeholder': ('First Name'), 'class': 'f_name'})

        self.fields['last_name'].widget.attrs.update(
            {'placeholder': ('Last Name'), 'class': 'l_name'})

        self.fields['email'].widget.attrs.update(
            {'placeholder': ('Email'), 'class': 'email'})

        self.fields['password1'].widget.attrs.update(
            {'placeholder': ('Password'), 'class': 'password1'})

        self.fields['password2'].widget.attrs.update(
            {'placeholder': ('Confirm Password'), 'class': 'password2'})

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')
