from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def games(request):
    context = {
        'games': [
            {'name': 'Atomic Heart', 'price': 1999},
            {'name': 'Cyberpunk 2077', 'price': 2499},
            {'name': 'PayDay 2', 'price': 999},
            {'name': 'Elden Ring', 'price': 2999},
            {'name': 'The Witcher 3: Wild Hunt', 'price': 1499},
        ]
    }
    return render(request, 'games.html', context)


class MainPage(TemplateView):
    template_name = 'main.html'

class CartPage(TemplateView):
    template_name = 'cart.html'