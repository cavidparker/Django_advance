from django.shortcuts import render
from .models import Contact, Post
from .forms import ContactForm, PostForm
from django.http.response import HttpResponse

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



def postview(request):
    post = Post.objects.all()
    return render(request, 'tuition/postview.html', {'post':post})


def postcreate(request):
    if request.method=="POST":
        form=PostForm(request.POST,request.FILES )
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            sub = form.cleaned_data['subject']
            for i in sub:
                obj.subject.add(i)
                obj.save()
            class_in = form.cleaned_data['class_in']
            for i in class_in:
                obj.class_in.add(i)
                obj.save()
            return HttpResponse("Success")    

    else:
        form = PostForm()
    return render(request, 'tuition/postcreate.html', {'form':form})


