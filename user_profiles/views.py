from django.shortcuts import render, get_object_or_404

from .models import Profile


def user_profiles(request):
    """ Displays the User's profile"""
    profile = get_object_or_404(Profile, user=request.user)
    context = {
        'profile': profile,
    }

    return render(request, 'user_profiles/profile.html', context)
