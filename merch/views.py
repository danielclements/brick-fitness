from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Product, Category


# Create your views here.


def all_merch(request):
    """ This view returns the Merch page """
    products = Product.objects.all()
    categories_all = Category.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)
    context = {
        'products': products,
        'categories_all': categories_all,
        'categories': categories,
    }
    return render(request, 'merch/merch.html', context)


def merch_detail(request, product_id):
    """ This view returns the individual merch detail page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'merch/merch_detail.html', context)
