from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


def search(request):
    if request.method=="POST":
        searched=request.POST['searched']
        products=Product.get_all_products_by_name('search')
        return render(request,'search.html',{'searched':searched,'products':products})
    else:
        return render(request,'search.html',{})