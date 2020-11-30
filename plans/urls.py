from django.urls import path
from . import views

urlpatterns = [
    path('nutrition', views.nutrition_plan, name='nutrition'),
    path('workoutplans', views.workout_plan, name='workoutplans'),
    path('<int:plans_id>', views.individual_plan, name='individual_plans'),
    path('activate/<int:plans_id>/', views.activate_plan, name='activate_plan'),
    path('activate/workout/<int:plan_id>/', views.activate_workout_plan, name='activate_workout_plan'),
]
