from django.shortcuts import render
from task1.models import *

# Create your views here.

def glavn_stran(request):
    lice_1 = 'Главная'
    lice_2 = 'Магазин'
    lice_3 = 'Корзина'
    context = {'title_lice': lice_1,
               'shop': lice_2,
               'corzina': lice_3}
    return render(request, 'Glavn.html', context)


def shop_stran(request):
    games = Game.objects.all()
    lice_1 = 'Главная'
    lice_2 = 'Магазин'
    lice_3 = 'Корзина'
    context = {'games': games,
               'title_lice': lice_1,
               'shop': lice_2,
               'corzina': lice_3}
    return render(request, 'Shop.html', context)


def corzina_stran(request):
    len_corz = 0
    lice_1 = 'Главная'
    lice_2 = 'Магазин'
    lice_3 = 'Корзина'
    context = {'len_corz': len_corz,
               'title_lice': lice_1,
               'shop': lice_2,
               'corzina': lice_3}
    return render(request, 'Corzina.html', context)