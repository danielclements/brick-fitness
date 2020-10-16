from django.shortcuts import render

# Create your views here.


def subscriptionPlans(request):
    """ This view returns the subscription home page """
    return render(request, 'subscriptions/subscription-plans.html')
