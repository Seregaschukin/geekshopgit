from django.shortcuts import render
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')

def products(request):
    return render(request, 'mainapp/products.html')

def test(request):
    context = {
        'title': 'geekshop',
        'header': 'Добро пожаловать',
        'user': 'Сергей',
        'date': datetime.today(),
        'products': [{'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00'},
                    {'name': 'Синяя куртка The North Face', 'price': '23 725,00'},
                    {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00'},

    ],
        'products_promo': [{'name': 'Черный рюкзак Nike Heritage', 'price': '5864'},
                     {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '21111'}
    ]
    }
    return render(request, 'mainapp/test.html', context)