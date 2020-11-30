import stripe
import logging
import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from subscriptions.webhook_handler import StripeWH_Handler


stripe.api_key = settings.STRIPE_SECRET_KEY
priceID = settings.STRIPE_PLAN_ANNUAL_ID
logger = logging.getLogger(__name__)


# Create your views here.

@csrf_exempt
def subscription_plans(request):
    """ This view returns the subscription home page """
    return render(request, 'subscriptions/subscription-plans.html')


@csrf_exempt
def checkout(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': priceID,
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('subscriptions')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('subscriptions')),
    )
    return JsonResponse({
        'session_id': session.id,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })


# stripe docs code, slightly altered using code
# # from Code Institute stripe tutorial
# @require_POST
# @csrf_exempt
# def my_webhook_view(request):
#     payload = request.body
#     event = None
#
#     try:
#         event = stripe.Event.construct_from(
#             json.loads(payload), stripe.api_key
#         )
#     except ValueError as e:
#         # Invalid payload
#         return HttpResponse(status=400)
#     except stripe.error.SignatureVerificationError as e:
#         # Invalid signature
#         return HttpResponse(status=400)
#
#     except Exception as e:
#         return HttpResponse(content=e, status=400)
#
#     # Set up webhook handler
#     handler = StripeWH_Handler(request)
#
#     event_map = {
#         'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
#         'payment_intent.failed': handler.handle_payment_intent_failed,
#     }
#
#     event_type = event['type']
#     event_handler = event_map.get(event_type, handler.handle_event)
#
#     response = event_handler(event)
#     return response
#

