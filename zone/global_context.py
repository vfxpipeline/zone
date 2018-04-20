from profiles.models import Profile


def logged_in_profile_settings(request):
    user = request.user
    if user.is_anonymous() or user.is_superuser:
        return {}
    profile = Profile.objects.get(user=user.profile.id)
    context = {
        "profile": profile,
    }
    return context
