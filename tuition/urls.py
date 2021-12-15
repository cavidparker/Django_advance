from django.urls import path
from .views import contact, postview,postcreate


urlpatterns = [
    path('contact/',contact,name="contact"),
    path('posts/',postview,name="posts"),
    path('create/',postcreate,name="create"),

]
