from django.shortcuts import render


def user_profiles(request):
    """ Displays the User's profile"""

    context = {}

    return render(request, 'user_profiles/profile.html', context)
