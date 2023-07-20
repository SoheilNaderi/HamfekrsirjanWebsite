
from django.urls import path
import website
from website.views import *

app_name='website'

urlpatterns = [
    path('',home,name='index'),#< veÿy importent ,,,,,,,,
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
    path ('jsontest',jsontest)
]
