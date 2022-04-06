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
    return False