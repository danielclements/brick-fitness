from django.shortcuts import render


# Create your views here.


def all_merch(request):
    """ This view returns the Merch page """
    return render(request, 'merch/merch.html')
