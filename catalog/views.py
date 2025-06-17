from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Category
from django.shortcuts import get_object_or_404


# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {
        'prods': products
    }
    return render(request, 'catalog/home.html', context=context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        return HttpResponse(f'Спасибо {name}, с номером "{phone}" и сообщением "{message}". Данные в сохранность!)')
    return render(request, 'catalog/contacts.html')


def product_details(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product
    }

    return render(request, 'catalog/product_details.html', context=context)


def to_add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        image = request.FILES.get('image')

        category = Category.objects.get(id=category_id)

        Product.objects.create(
            name=name,
            description=description,
            price=price,
            category=category,
            image=image
        )

        return redirect('home')

    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'catalog/to_add_product.html', context=context)
