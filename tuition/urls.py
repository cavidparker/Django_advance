from django.urls import path
from .views import contact, postview,postcreate,subview,classview,ContactView, PostCreateView,PostListView,PostDetailView,PostEditView,PostDeleteView
from .forms import ContactFormthree


urlpatterns = [
    path('contact/',contact,name="contact"),
    path('contact_classbased/',ContactView.as_view(),name="contact_classbased"),
   # path('contact_classbased3/',ContactView.as_view(form_class=ContactFormthree, template_name= "contact3.html"),name="contact_classbased3"),

    path('posts/',postview,name="posts"),
    path('postlist/',PostListView.as_view(),name="postlist"),
    path('postdetail/<int:pk>/',PostDetailView.as_view(),name="postdetail"),
    path('edit/<int:pk>/',PostEditView.as_view(),name="edit"),
    path('delete/<int:pk>/',PostDeleteView.as_view(),name="delete"),





    path('subjects/',subview,name="subject"),
    path('classes/',classview,name="classes"),
    # path('create/',postcreate,name="create"),
    path('create/',PostCreateView.as_view(),name="create"),


]
