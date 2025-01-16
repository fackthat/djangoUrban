from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

# def func_template(request):
#     return render(request, 'func_template.html')

class MainPage(TemplateView):
    template_name = 'main.html'

class ShopPage(TemplateView):
    template_name = 'games.html'

class CartPage(TemplateView):
    template_name = 'cart.html'