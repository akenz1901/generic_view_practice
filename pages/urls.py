from .views import HomePageView, sendAbout
from django.urls import path

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', sendAbout, name='about')
]
