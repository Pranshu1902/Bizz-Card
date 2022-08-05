from django.shortcuts import render
from cards.models import Card
from django.views.generic.list import ListView
# Create your views here.


# home page view
class HomePageView(ListView):
    model = Card
    template_name = "home.html"
    context_object_name = "card"
    login_url = "/login/"
