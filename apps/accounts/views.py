from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.exceptions import ValidationError

from .forms import LoginForm, RegisterForm
from apps.accounts.models import User
from .mixins import LogoutRequiredMixin

import sweetify

class RegisterView(LogoutRequiredMixin, View):
    def get(self, request):
        form = RegisterForm()
        context = {"form": form}
        return render(request, "accounts/register.html", context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            if password1 != password2:
                # Add the password do not match to the forms errors
                form.add_error("password2", "Passwords do not match")
            else:
                user = form.save()
                return redirect("login")
        context = {"form": form}
        return render(request, "accounts/register.html", context)


class LoginView(LogoutRequiredMixin, View):
    def get(self, request):
        form = LoginForm()
        context = {"form": form}
        return render(request, "accounts/login.html", context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)

            if not user:
                messages.error(request, "Invalid Credentials")
                return redirect("login")
            
            login(request, user)
            return redirect("/")
        context = {"form": form}
        return render(request, "accounts/login.html", context)


class LogoutUserView(View, LogoutRequiredMixin):
    def get(self, request):
        logout(request)
        return redirect(reverse("login"))
