from django import forms
from .models import*


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