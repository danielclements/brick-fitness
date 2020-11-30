from django.http import HttpResponse
from user_profiles.models import Profile



class StripeWH_Handler:
    """Handle incoming stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle generic and unexpected webhooks"""
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """Handle successful payment intent webhooks"""
        Profile.objects.update(subscription_premium=True)
        print("payment success")

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_failed(self, event):
        """Handle failed payment intent webhooks"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_charge_succeeded(self, event):
        """handle the accepted charge response"""
