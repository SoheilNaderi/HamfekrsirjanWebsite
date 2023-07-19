
from django.urls import path
from website.views import *

urlpatterns = [
    path('',home),#< veÿy importent ,,,,,,,,
    path('about',about),
    path('contact',contact),
    path ('jsontest',jsontest)
]
