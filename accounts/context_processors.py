# accounts/context_processors.py

from .models import UserProfile


def user_profile(request):
    """Context processor to add user profile to the context."""
    profile = None
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            pass
    return {"profile": profile}
