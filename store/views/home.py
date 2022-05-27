from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.customer import Customer
from store.models.product import Product
from store.models.category import Category
from django.views import View

from store.models.room import Room



# Create your views here.
class Index(View):
    def get(self , request):
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')

    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories    

    if request.method == 'POST':
        min_price = request.POST.get('min_price')
        max_price = request.POST.get('max_price')
        if min_price == '':
            min_price = 1
        if max_price == '':
            max_price = 1
        categories = Category.get_all_categories()

          
        products = Product.get_product_by_price(int(min_price), int(max_price))
        data = {}
        data['products'] = products
        data['categories'] = categories  
        return render(request, 'index.html', data)

    return render(request, 'index.html', data)


