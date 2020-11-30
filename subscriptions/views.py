import stripe
import logging

from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from user_profiles.models import Profile
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)


# Create your views here.

@csrf_exempt
def upgrade(request):
    """ This view returns the subscription home page """
    return render(request, 'subscriptions/subscription-plans.html')


# Credit Alex Ford and code institute please see read me
@login_required
def make_payment(request):
    """
    The form for processing the payment and sending the form to stripe.
    """

    profile = Profile.objects.get(user=request.user)

    if profile.subscription_premium:
        return redirect('profile')

    stripe_public_key = settings.STRIPE_PUBLISHABLE_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_total = 2999

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    if request.method == 'POST':
        profile.subscription_premium = True
        profile.save()

        return redirect('payment_successful')

    return render(request, 'subscriptions/payment.html', context)

@login_required
def payment_successful(request):
    """
    Display payment successful page.
    """
    return render(request, 'subscriptions/payment-success.html')
