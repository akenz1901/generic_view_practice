from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = 'home.html'


def sendAbout(request):
    return render(request, './about.html')
