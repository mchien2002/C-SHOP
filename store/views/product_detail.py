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
        color = request.POST.get('product_color')

        cart = request.session.get('cart')
        error_message = self.validateProductDetail(size, color)
        
        if not error_message:
            productDetail = ProductDetail(
                product = product,
                size = size,
                color = color
            )

            if quantity == '':
                quantity = 1
            if ProductDetail.isExist(productDetail) == False:
                productDetail.save()
            else:
                productDetail = ProductDetail.get_productDetail_by_product_and_size(product, size, color)
            if cart:
                quantity_in_cart = cart.get(str(productDetail.id))
                if quantity_in_cart:
                    cart[productDetail.id]  = quantity_in_cart + int(quantity)
                else:
                    cart[productDetail.id] = int(quantity)
            else:
                cart = {}
                cart[productDetail.id] = int(quantity)
            request.session['cart'] = cart
            return redirect('cart')
        else:
            data = {
                'error': error_message,
                'product': product 
            }
            return render(request, 'product_detail.html', data)

    def validateProductDetail(self, size, color):
        error_message = None
        if size == None and color == None:
            error_message = "Hãy chọn size và màu cho sản phẩm"
        elif size == None:
            error_message = "Hãy chọn size cho sản phẩm"
        elif color == None:
            error_message = "Hãy chọn màu cho sản phẩm"

        return error_message