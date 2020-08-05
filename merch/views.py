from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.


def all_merch(request):
    """ This view returns the Merch page """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'merch/merch.html', context)


def merch_detail(request, product_id):
    """ This view returns the individual merch detail page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'merch/merch_detail.html', context)
