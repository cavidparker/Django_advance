from django.urls import path
from .views import contact, postview,postcreate,subview,classview


urlpatterns = [
    path('contact/',contact,name="contact"),
    path('posts/',postview,name="posts"),
    path('subjects/',subview,name="subject"),
    path('classes/',classview,name="classes"),
    path('create/',postcreate,name="create"),

]
