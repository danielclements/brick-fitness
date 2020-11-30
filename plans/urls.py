from django.urls import path
from . import views

urlpatterns = [
    path('', views.plans, name='plans'),
    path('<plans_id>', views.individual_plan, name='individual_plans'),
]
