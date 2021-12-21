from django.shortcuts import render
from .models import Contact, Post, Subject, Class_in
from .forms import ContactForm, PostForm
from django.http.response import HttpResponse
from django.views import View

##### Class Based Form View #####
from django.views.generic import FormView
from django.urls import reverse_lazy

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    # success_url = '/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('homeview')


from django.views.generic import CreateView

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'tuition/postcreate.html'
    # success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('posts')

##### CLASS BASED VIEWS #####
# class ContactView(View):
#     form_class = ContactForm
#     template_name = 'contact.html'
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("successfully saved")
#         return render(request, self.template_name, {'form': form})



##### FUNCTION BASED VIEWS #####
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


### Using list view to post the data
from django.views.generic import ListView
class PostListView(ListView):
    template_name = 'tuition/postlist.html'
    # model = Post
    queryset = Post.objects.filter(user=2)
    context_object_name = 'posts'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['posts'] = context.get('object_list')
        context['msg'] = 'This is host list'
        return context

def postview(request):
    post = Post.objects.all()
    return render(request, 'tuition/postview.html', {'post':post})


def subview(request):
    sub = Subject.objects.all()
    return render(request, 'tuition/subjectview.html', {'sub':sub})


def classview(request):
    class_in = Class_in.objects.all()
    return render(request, 'tuition/classview.html', {'class_in':class_in})


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


