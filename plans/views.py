from django.shortcuts import render
from .models import MealPlan


# Create your views here.
def plans(request):
    """ This view returns the plans home page """

    mealplans = MealPlan.objects.all()
    context = {
        'mealplans': mealplans
    }
    return render(request, 'plans/plans.html', context)
