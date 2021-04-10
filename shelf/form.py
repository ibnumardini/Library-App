from django import forms
from shelf import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class BookForm(forms.ModelForm):

    class Meta:
        model = models.Book
        fields = '__all__'
        
        widgets = {
            'title' : forms.TextInput({'class':'form-control'}),
            'writer' : forms.TextInput({'class':'form-control'}),
            'publisher' : forms.TextInput({'class':'form-control'}),
            'amount' : forms.NumberInput({'class':'form-control'}),
            'group' : forms.Select({'class':'form-control'}),
        }

class GroupForm(forms.ModelForm):

    class Meta:
        model = models.Group
        fields = '__all__'
        
        widgets = {
            'name' : forms.TextInput({'class':'form-control'}),
            'description' : forms.Textarea({'class':'form-control'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'})) 

class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'})) 
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'})) 
    