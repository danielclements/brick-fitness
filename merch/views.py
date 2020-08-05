from django.shortcuts import render
from .models import Product


# Create your views here.

products = Product.objects.all()

context = {
    'products': products,
}


def all_merch(request):
    """ This view returns the Merch page """
    return render(request, 'merch/merch.html', context)
