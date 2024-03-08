from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.exceptions import ValidationError

from .forms import LoginForm, RegisterForm
from apps.accounts.models import User

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context = {
            "form":form
        }
        return render(request, 'accounts/register.html', context)
    
    def post(self, request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 != password2:
                # Add the passwordd do not match to the forms errors
                form.add_error('password2', "Passwords do not match")
            else:
                user = form.save()
                return redirect('login') 
        context = {
            "form":form
        }
        return render(request, 'accounts/register.html', context)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            "form":form
        }
        return render(request, 'accounts/login.html', context)
    
    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
          email = form.cleaned_data["email"]
          password = form.cleaned_data["password"]

          user = authenticate(email=email, password=password)
          if not user:
              messages.error(request, "Email or password Incorrect")
              return redirect("login")
          login(request, user)
          return redirect("/")

        return render(request, 'accounts/login.html')



