from math import prod
from django.shortcuts import redirect, render
from django.views import View

from store.models.product import Product
from store.models.product_detail import ProductDetail

class ProductDetailViews(View):
    
    def get(self, request):
        product_id = request.GET.get('product_id')
        product = Product.objects.get(id = product_id)

        return render(request, 'product_detail.html', {'product': product})

    def post(self, request):
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id = product_id)
        size = request.POST.get('product_size')
        quantity = request.POST.get('quantity')
        cart = request.session.get('cart')

        productDetail = ProductDetail(
            product = product,
            size = size
        )

        if ProductDetail.isExist(productDetail) == False:
            productDetail.save()
        else:
            productDetail = ProductDetail.get_productDetail_by_product_and_size(product, size)
        if cart:
            quantity_in_cart = cart.get(str(productDetail.id))
            if quantity_in_cart:
                cart[productDetail.id]  = quantity_in_cart + int(quantity)
            else:
                cart[productDetail.id] = int(quantity)
        else:
            cart = {}
            cart[productDetail.id] = 1
        request.session['cart'] = cart
        
        return redirect('cart')