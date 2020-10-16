from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscriptionPlans, name='subscription-plans'),
]
