from user_profiles.models import Profile


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if Profile.subscription_premium:
        delivery = 0
    else:
        delivery = 5.99

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
