from django.shortcuts import render

# Create your views here.
def plans(request):
    """ This view returns the plans home page """
    return render(request, 'plans/plans.html')