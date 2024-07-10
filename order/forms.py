#created new
from django import forms
from .models import Orders

INPUT_CLASSES='w-full py-4 px-6 rounded-xl border'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['payment_method',  'quantity_of_items']
        widgets = {
        'payment_method': forms.TextInput(attrs={
            'class': 'form-control'}),
        'quantity_of_items': forms.NumberInput(attrs={
            'class': 'form-control'}),
        'price': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
        }