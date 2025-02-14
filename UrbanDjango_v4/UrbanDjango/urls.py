"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# TASK2
# from django.contrib import admin
# from django.urls import path
# from task2.views import func_template, ClassTemplate
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', func_template),
#     path('page/', ClassTemplate.as_view()),
# ]

# TASK3
# from django.contrib import admin
# from django.urls import path
# from task3.views import MainPage, ShopPage, CartPage
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', MainPage.as_view()),
#     path('shop/', ShopPage.as_view()),
#     path('cart/', CartPage.as_view()),
# ]

# TASK4
from django.contrib import admin
from django.urls import path
from task4.views import MainPage, CartPage, games

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view()),
    path('cart/', CartPage.as_view()),
    path('games/', games),
]
