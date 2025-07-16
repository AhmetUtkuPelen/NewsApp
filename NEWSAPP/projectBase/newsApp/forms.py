from django import forms
from .models import*
from django.contrib.auth.models import User

# ! FOR USERS TO CREATE THEIR OWN NEWS ! #

class CreateUserNewsForm(forms.ModelForm):


    class Meta:
        model = UserCreateNews
        fields = ['title','description','image']
        
        
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control border border-1 border-primary mt-2 text-center'}),
            'owner' : forms.TextInput(attrs={'class':'text-uppercase text-danger text-center mt-2'}),
            'description' : forms.TextInput(attrs={'class':'text-uppercase text-center form-control mt-2'}),
            'image': forms.FileInput(attrs={'class':'mt-4 form-control'}),
        }






# ! FOR USERS TO EDIT THEIR PROFILES ! #
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control border border-1 border-primary mt-2 text-center'}),
            'email': forms.EmailInput(attrs={'class': 'form-control border border-1 border-primary mt-2 text-center'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control border border-1 border-primary mt-2 text-center'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control border border-1 border-primary mt-2 text-center'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'mail', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
