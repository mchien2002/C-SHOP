from atexit import register
from django import template

register = template.Library()
@register.filter(name = 'is_in_cart')

# Chien: Hàm is_in_cart xác định xem sản phẩm đó đã có trong dỏ hàng chưa
def is_in_cart(product, cart):
    # Chien: select tất cả các product có trong cart
    keys = cart.keys()
    # Chien: id là số lượng mua của từng product
    for id in keys:
        print(id, product.id)
        print(type(id), type(product.id))
        
        if int(id) == product.id:
            return True
    return False;

@register.filter(name = 'cart_quantity')
def cart_quantity(product, cart):
    # Hoang: đếm số lượng sản phẩm trong giỏ hàng
    keys = cart.keys()
    # Hoang: id là số lượng mua của từng product
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0;