from django.urls import path
from . import views

urlpatterns = [
    path('', views.plans, name='plans'),
    path('<int:plans_id>', views.individual_plan, name='individual_plans'),
    path('activate/<int:plans_id>/', views.activate_plan, name='activate_plan'),
]
