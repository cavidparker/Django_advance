from django.shortcuts import render, HttpResponse
# from tuition.models import Contact

def home(request):
    # return HttpResponse('Hello World')
    if request.method == 'GET':
        name = ['John', 'Jane', 'Joe', 'max']
    else: 
        name= []   
    context = {
        'name': name
    }
    return render(request, 'home.html', context)

### one way to do it and save the data in the database using models

# def contact(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         phone = request.POST['phone']
#         content = request.POST['content']
#         print(name)
#         print(phone)
#         print(content)
#         obj = Contact(name=name, phone=phone, content=content)
#         obj.save()
#     return render(request, 'contact.html')


from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg'] = 'This is home page'
        context['msg2'] = 'welcome to home page'

        return context