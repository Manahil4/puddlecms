from django import forms
from .models import DesignerProfile

class DesignerProfileForm(forms.ModelForm):
    class Meta:
        model = DesignerProfile
        fields = ['experience','specialization','bio', 'previous_work', 'education', 'portfolio_image']
    experience=forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Your experience',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    specialization=forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Your specialization',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    bio = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Your Bio',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    previous_work = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Your Previous Work',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    education = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Your Education',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    portfolio_image = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
