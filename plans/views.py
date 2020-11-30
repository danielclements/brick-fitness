from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import MealPlan
from user_profiles.models import Profile
from user_profiles.views import user_profiles


# Create your views here.
def plans(request):
    """ This view returns the plans home page """

    mealplans = MealPlan.objects.all()
    context = {
        'mealplans': mealplans
    }
    return render(request, 'plans/plans.html', context)


def individual_plan(request, plans_id):
    """ This view returns the individual merch detail page """

    plan = get_object_or_404(MealPlan, pk=plans_id)

    context = {
        'plan': plan,
    }
    return render(request, 'plans/invidual-plan.html', context)


def activate_plan(request, plans_id):
    """ This view returns the individual merch detail page """
    plan = get_object_or_404(MealPlan, pk=plans_id)
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        profile.active_meal_plan = plan
        profile.save()
        return redirect(user_profiles)



