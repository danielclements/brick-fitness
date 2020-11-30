from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscription_plans, name='subscriptions'),
    path('make_payment/', views.make_payment, name='make_payment'),
    path('payment_successful/', views.payment_successful, name='payment_successful'),
    # path('stripe-webhooks', views.my_webhook_view, name='stripe_webhooks'),
]
