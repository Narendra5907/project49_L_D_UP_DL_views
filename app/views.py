from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import TemplateView
from django.views.generic import ListView
class Home(TemplateView):
    template_name='app/Home.html'



class School_list(ListView):
    model=School
    # template_name='app/school_list.html'
    context_object_name='schools'