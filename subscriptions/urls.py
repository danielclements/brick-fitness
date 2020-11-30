from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscription_plans, name='subscriptions'),
    # path('stripe-webhooks', views.my_webhook_view, name='stripe_webhooks'),
    path('checkout', views.checkout, name='checkout'),

]
