from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View



# Create your views here.
class Index(View):

    def post(self , request):
        id_product = request.POST.get('product')
        product = Product.objects.get(id = id_product)
        size = request.POST.get('size')
        product.size = size
        product.save()
        remove = request.POST.get('remove') 
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(id_product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(id_product)
                    else:
                        cart[id_product]  = quantity-1
                else:
                    cart[id_product]  = quantity+1

            else:
                cart[id_product] = 1
        else:
            cart = {}
            cart[id_product] = 1
        request.session['cart'] = cart
        return redirect('homepage')



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

