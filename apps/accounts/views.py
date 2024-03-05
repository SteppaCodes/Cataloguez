from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from .forms import LoginForm


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


