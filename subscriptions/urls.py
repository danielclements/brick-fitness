from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscription_plans, name='subscriptions'),
    path('subscription-type', views.subscription_selection, name='subscription-type'),
    path('payment-method', views.payment_method, name='payment_method'),
    path('card', views.card, name='card'),
    path('stripe-webhooks', views.stripe_webhooks, name='stripe_webhooks'),
]
