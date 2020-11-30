from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import MealPlan, WorkOutPlan
from user_profiles.models import Profile
from user_profiles.views import user_profiles


# Create your views here.
def nutrition_plan(request):
    """ This view returns the plans home page """

    mealplans = MealPlan.objects.all()
    context = {
        'mealplans': mealplans
    }
    return render(request, 'plans/plans.html', context)


def workout_plan(request):
    """ This view returns the plans home page """

    workoutplans = WorkOutPlan.objects.all()
    context = {
        'workoutplans': workoutplans
    }
    return render(request, 'plans/work-plans.html', context)


def individual_plan(request, plans_id):
    """ This view returns the individual merch detail page """

    plan = get_object_or_404(MealPlan, pk=plans_id)

    context = {
        'plan': plan,
    }
    return render(request, 'plans/invidual-plan.html', context)


def individual_workout(request, plan_id):
    """ This view returns the individual merch detail page """

    plan = get_object_or_404(WorkOutPlan, pk=plan_id)

    context = {
        'plan': plan,
    }
    return render(request, 'plans/individual-workout.html', context)


def activate_plan(request, plans_id):
    """ This view returns the individual merch detail page """
    plan = get_object_or_404(MealPlan, pk=plans_id)
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        profile.active_meal_plan = plan
        profile.save()
        return redirect(user_profiles)


def activate_workout_plan(request, plan_id):
    """ This view returns the individual merch detail page """
    plan = get_object_or_404(WorkOutPlan, pk=plan_id)
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        profile.active_workout_plan = plan
        profile.save()
        return redirect(user_profiles)



