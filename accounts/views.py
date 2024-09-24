from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm  # Create this form to handle user profile updates
# accounts/views.py

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import UserProfile  # Ensure you import UserProfile here


def signup_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        phone = request.POST.get("phone")  # Get the phone number from the POST data

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            # Create UserProfile instance for the new user
            UserProfile.objects.create(user=user, phone=phone)  # Pass the phone number

            messages.success(request, "Registration successful! You can now log in.")
            return redirect("accounts:login")  # Redirect to login page
    else:
        form = UserRegistrationForm()

    return render(request, "accounts/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Create a session for the user
            return redirect("dashboard")  # Redirect to home or dashboard
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)  # Log out the user
    return redirect("accounts:login")  # Redirect to the login page


@login_required
def profile_view(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            if form.cleaned_data.get("password"):
                user.set_password(
                    form.cleaned_data["password"]
                )  # Set the new password if provided
            user.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("accounts:profile")  # Redirect to profile page
    else:
        form = UserProfileForm(instance=request.user)

    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(
        request, "accounts/profile.html", {"user": request.user, "profile": profile}
    )


@login_required
def edit_profile_view(request):
    profile = UserProfile.objects.get(user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # Update user fields
            request.user.username = request.POST.get("username")
            request.user.email = request.POST.get("email")
            request.user.save()

            # Update UserProfile fields
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("accounts:profile")  # Redirect to profile view
    else:
        # If not POST, initialize the form with the existing profile
        form = UserProfileForm(instance=profile)

    return render(request, "accounts/edit_profile.html", {"form": form})
