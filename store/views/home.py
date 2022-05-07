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
        products = Product.get_all_products();

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    

    return render(request, 'index.html', data)


