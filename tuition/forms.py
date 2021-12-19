from django import forms
from .models import Contact, Post



#### form 
# class ContactForm(forms.Form):
#     name = forms.CharField(label='Your name', max_length=100)
#     phone = forms.CharField(label='Your Phone', max_length=100)
#     content = forms.CharField(label='Your Details', max_length=100)


#### class based form #####

class ContactFormthree(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'




#### function based views use form #####
#### modelform
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        # fields = ['name', 'phone', 'content']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','id','created_at','slug',]
        widgets ={
            'class_in': forms.CheckboxSelectMultiple(attrs={
                'multiple': True,
            }),
            'subject': forms.CheckboxSelectMultiple(attrs={
                'multiple': True,
            })
        }