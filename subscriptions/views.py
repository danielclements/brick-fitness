import stripe
import logging
import json
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from subscriptions.payments.stripe import SubPlan
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from subscriptions.webhook_handler import StripeWH_Handler

API_KEY = settings.STRIPE_SECRET_KEY
logger = logging.getLogger(__name__)


# Create your views here.


def subscription_plans(request):
    """ This view returns the subscription home page """
    return render(request, 'subscriptions/subscription-plans.html')


def subscription_selection(request):
    """ This view returns the subscription selection box, giving the user the option
    between a monthly sub or a annual sub"""
    return render(request, 'subscriptions/subscription_type.html')


# stripe docs code, slightly altered using code
# from Code Institute stripe tutorial
@require_POST
@csrf_exempt
def my_webhook_view(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Set up webhook handler
    handler = StripeWH_Handler(request)

    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.failed': handler.handle_payment_intent_failed,
    }

    event_type = event['type']
    event_handler = event_map.get(event_type, handler.handle_event)

    response = event_handler(event)
    return response


# Stripe payments with django on youtube by DjangoLessons,
# Please visit readme to find a link to this channel
@require_POST
@login_required
def payment_method(request):
    stripe.api_key = API_KEY
    plan = request.POST.get('plan', 'm')
    automatic = request.POST.get('automatic', 'on')
    payment_method = request.POST.get('payment_method', 'card')
    context = {}

    plan_inst = SubPlan(plan_id=plan)
    #               plan_inst.amount
    # 'a' | 'm' =>  plan_inst.currency
    #               plan_inst.stripe_plan_id

    payment_intent = stripe.PaymentIntent.create(
        amount=plan_inst.amount,
        currency=plan_inst.currency,
        payment_method_types=['card']
    )

    if payment_method == 'card':

        context['secret_key'] = payment_intent.client_secret
        context['STRIPE_PUBLISHABLE_KEY'] = settings.STRIPE_PUBLISHABLE_KEY
        context['customer_email'] = request.user.email
        context['payment_intent_id'] = payment_intent.id
        context['automatic'] = automatic
        context['stripe_plan_id'] = plan_inst.stripe_plan_id

        return render(request, 'subscriptions/card.html', context)


@login_required
def card(request):

    payment_intent_id = request.POST['payment_intent_id']
    payment_method_id = request.POST['payment_method_id']
    stripe_plan_id = request.POST['stripe_plan_id']
    automatic = request.POST['automatic']
    stripe.api_key = API_KEY

    if automatic == 'on':
        # create subs
        customer = stripe.Customer.create(
            email=request.user.email,
            payment_method=payment_method_id,
            invoice_settings={
                'default_payment_method': payment_method_id
            }
        )
        s = stripe.Subscription.create(
            customer=customer.id,
            items=[
                {
                    'plan': stripe_plan_id
                },
            ]
        )
        latest_invoice = stripe.Invoice.retrieve(s.latest_invoice)

        ret = stripe.PaymentIntent.confirm(
            latest_invoice.payment_intent
        )

        if ret.status == 'requires_action':
            pi = stripe.PaymentIntent.retrieve(
                latest_invoice.payment_intent
            )
            context = {}

            context['payment_intent_secret'] = pi.client_secret
            context['STRIPE_PUBLISHABLE_KEY'] = settings.STRIPE_PUBLISHABLE_KEY

            return render(request, 'subscriptions/3dsec.html', context)
    else:
        stripe.PaymentIntent.modify(
            payment_intent_id,
            payment_method=payment_method_id
        )

    return render(request, 'user_profiles/profile.html')