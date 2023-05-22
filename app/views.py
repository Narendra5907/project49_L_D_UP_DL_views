from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import *



class Home(TemplateView):
    template_name='app/Home.html'



class School_list(ListView):
    model=School
    # template_name='app/school_list.html'
    context_object_name='schools'
class School_Detail(DetailView):
    model=School
    context_object_name='sclobject'


class School_Create(CreateView):
    model=School
    fields='__all__'
