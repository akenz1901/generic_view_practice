from django.views.generic import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = 'home.html'


def sendAbout(request):
    return render(request, './about.html')
