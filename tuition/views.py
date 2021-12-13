from django.shortcuts import render
from .models import Contact
from .forms import ContactForm

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # name = form.cleaned_data['name']
            # phone = form.cleaned_data['phone']
            # content = form.cleaned_data['content']
            # print(name)
            # print(phone)
            # print(content)
            # obj = Contact(name=name, phone=phone, content=content)
            # obj.save()
    else:
        form = ContactForm()    


    return render(request, 'contact2.html',{'form':form})  