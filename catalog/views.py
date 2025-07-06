from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Product, Category
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import ProductForm


class ProductListView(ListView):
    model = Product
    context_object_name = 'prods'


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    extra_context = {'categories': Category.objects.all()}
    success_url = reverse_lazy('catalog:home')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    extra_context = {'categories': Category.objects.all()}
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:home')


class ContactView(View):
    template_name = 'catalog/contacts.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f'Спасибо {name}, с номером "{phone}" и сообщением "{message}". Данные в сохранность!')

        return HttpResponseRedirect(reverse_lazy('catalog:home'))

# def home(request):
#     products = Product.objects.all()
#     context = {
#         'prods': products
#     }
#     return render(request, 'catalog/home.html', context=context)


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#
#         return HttpResponse(f'Спасибо {name}, с номером "{phone}" и сообщением "{message}". Данные в сохранность!)')
#     return render(request, 'catalog/contacts.html')


# def product_details(request, product_id):
#
#     product = get_object_or_404(Product, id=product_id)
#     context = {
#         'product': product
#     }
#
#     return render(request, 'catalog/product_detail.html', context=context)


# def to_add_product(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         price = request.POST.get('price')
#         category_id = request.POST.get('category')
#         image = request.FILES.get('image')
#
#         category = Category.objects.get(id=category_id)
#
#         Product.objects.create(
#             name=name,
#             description=description,
#             price=price,
#             category=category,
#             image=image
#         )
#
#         return redirect('home')
#
#     categories = Category.objects.all()
#     context = {
#         "categories": categories
#     }
#     return render(request, 'catalog/product_form.html', context=context)
