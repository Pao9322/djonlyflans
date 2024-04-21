from django import forms

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='Email')
    customer_name = forms.CharField(max_length=64, label='Name')
    message = forms.CharField(label='Message')