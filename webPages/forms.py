from django import forms
from .models import ContactForm

#clase del formulario que se visualizará en la web

class ContactFormForm(forms.ModelForm): 
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
