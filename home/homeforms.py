from django import forms

class ContactForm(forms.Form):
    Message = forms.CharField()
    Email = forms.EmailField()