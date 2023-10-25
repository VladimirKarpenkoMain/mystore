from django.shortcuts import render


def index(request):
    return render(request, 'products/index.html')


def products(request):
    context = {'title': 'Store',
               'products': [
                   {
                       'name': 'Худи черного цвета с монограммами adidas Originals',
                       'imagine': 'static/vendor/img/products/Adidas-hoodie.png',
                       'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
                       'price': 6090,
                   },

                   {
                       'name': 'Синяя куртка The North Face',
                       'imagine': 'static/vendor/img/products/Blue-jacket-The-North-Face.png',
                       'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                       'price': 23725,
                   },

                   {
                       'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                       'imagine': 'static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                       'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
                       'price': 3390,
                   },

                   {
                       'name': 'Синяя куртка The North Face',
                       'imagine': 'static/vendor/img/products/Blue-jacket-The-North-Face.png',
                       'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                       'price': 23725,
                   }
               ]}
    return render(request, 'products/products.html')
