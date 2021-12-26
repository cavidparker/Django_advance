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
    name=forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your name'}), label='Your name') 
    class Meta:
        model = Contact
        fields = '__all__'
        # fields = ['name', 'phone', 'content']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].label='My Name'
        # self.fields['name'].initial='My Name'
        self.fields['phone'].initial='+8801'

    def clean_name(self):
        value=self.cleaned_data.get('name')
        num_of_w= value.split(' ')
        if len(num_of_w) > 3:
            self.add_error('name', 'Name can have maximun of 3 words')
        if value.isnumeric():
            self.add_error('name', 'Name can not be numeric')
        if len(value) < 3:
            self.add_error('name', 'Name should be at least 3 characters long')
        else:
            return value

    def clean_phone(self):
        value=self.cleaned_data.get('phone')
        if value.startswith('0'):
            self.add_error('phone', 'Phone number should not start with 0')
        if not value.startswith('+'):
            self.add_error('phone', 'Phone number should start with +')
        if len(value) != 14:
            self.add_error('phone', 'Phone number should be 13 characters long')
        else:
            return value


    def clean_content(self):
        value=self.cleaned_data.get('content')
        if len(value) < 5:
            self.add_error('content', 'Content should be at least 10 characters long')
        else:
            return value


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