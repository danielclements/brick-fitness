from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_merch, name='merch'),
    path('<product_id>', views.merch_detail, name='product_detail'),
]
