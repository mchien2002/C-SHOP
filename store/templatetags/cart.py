from atexit import register
from django import template

register = template.Library()

@register.filter(name='cart_quantity')
def cart_quantity(productDetail, cart):
    keys = cart.keys()
    # Hoang: id là số lượng mua của từng product
    for id in keys:
        if int(id) == productDetail.id:
            return cart.get(id)
    return 0


@register.filter(name='price_total')
def price_total(productDetail, cart):
    return productDetail.product.price * cart_quantity(productDetail, cart)


@register.filter(name='total_cart_price')
def total_cart_price(productDetails, cart):
    sum = 0
    for p in productDetails:
        sum += price_total(p, cart)
    return sum