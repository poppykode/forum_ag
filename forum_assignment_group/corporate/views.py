from django.shortcuts import render
from django.views.generic.list import ListView,View
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name ='corporate/home.html'

class AboutView(TemplateView):
    template_name ='corporate/about_us.html'

class ContactView(TemplateView):
    template_name ='corporate/contact_us.html'

class ExpertiseView(TemplateView):
    template_name ='corporate/our_expertise.html'

