from django import forms
from .models import Contact



#### form 
# class ContactForm(forms.Form):
#     name = forms.CharField(label='Your name', max_length=100)
#     phone = forms.CharField(label='Your Phone', max_length=100)
#     content = forms.CharField(label='Your Details', max_length=100)


#### modelform


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        # fields = ['name', 'phone', 'content']