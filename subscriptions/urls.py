from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscription_plans, name='subscriptions'),
    path('stripe-webhooks', views.my_webhook_view, name='stripe_webhooks'),
    path('subscription-type', views.subscription_selection, name='subscription-type'),
    path('payment-method', views.payment_method, name='payment_method'),
    path('card', views.card, name='card'),
]
