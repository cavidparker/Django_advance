from django.shortcuts import render
from .models import Contact, Post, Subject, Class_in
from .forms import ContactForm, PostForm
from django.http.response import HttpResponse
from django.views import View

##### Class Based Form View #####
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages


### Search Function ###
from django.db.models import Q
def search(request):
    query = request.POST.get('search', '')

    if query:
        queryset = (Q(title__icontains=query)) | (Q(details__icontains=query)) | (Q(medium__icontains=query)) | (Q(medium__icontains=query)) | (Q(category__icontains=query)) | Q(subject__name__icontains=query) | Q(class_in__name__icontains=query)
        results = Post.objects.filter(queryset).distinct()
    else:
        results = []
    context = {
        'results': results,
    }
    return render(request, 'tuition/search.html', context)  

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    # success_url = '/'
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you for your message. We will get back to you soon!')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('homeview')

#### Create view using generic view ####
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

##### Edit using generic view ####
from django.views.generic import UpdateView
class PostEditView(UpdateView):
    model=Post
    form_class=PostForm
    template_name='tuition/postcreate.html'
    def get_success_url(self):
        id = self.object.id
        return reverse_lazy('postdetail', kwargs={'pk': id})
### Delete using generic view ###
from django.views.generic import DeleteView
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'tuition/delete.html'
    success_url = reverse_lazy('postlist')




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


### Using detail view to display the post
from django.views.generic import DetailView
class PostDetailView(DetailView):
    model = Post
    template_name = 'tuition/postdetail.html'
    context_object_name = 'post'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['post'] = context.get('object_2')
        context['msg'] = 'This is post detail'
        return context


### Using listview to display the post
from django.views.generic import ListView
class PostListView(ListView):
    template_name = 'tuition/postlist.html'
    # model = Post
    # queryset = Post.objects.filter(user=1)
    queryset = Post.objects.all()
    context_object_name = 'posts'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['posts'] = context.get('object_list')
        context['subjects'] = Subject.objects.all() 
        context['classes'] = Class_in.objects.all()
        context['msg'] = 'This is post list'
        return context

#### Advance filter ####
def filter(request):
    subject = request.POST['subject']
    class_in = request.POST['class_in']
    print(subject, class_in)
    if subject or class_in:
        queryset = Q(subject__name__icontains=subject) | Q(class_in__name__icontains=class_in)
        results = Post.objects.filter(queryset).distinct()
    else:
        results = []
    context = {
        'results': results,
    }
    return render(request, 'tuition/search.html', context)    


#### Post view ###
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


