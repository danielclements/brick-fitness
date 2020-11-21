from django.shortcuts import render


def view_shopping_bag(request):

    return render(request, 'bag/bag.html')
