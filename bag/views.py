from django.shortcuts import render, redirect


def view_shopping_bag(request):

    return render(request, 'bag/bag.html')


# Code institute Code
def add_to_bag(request, item_id):
    """ Add products to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    if item_id in list (bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
# End of Code Institute Code
