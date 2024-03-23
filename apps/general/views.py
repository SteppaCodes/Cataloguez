from django.shortcuts import render, redirect
from django.views import View
import sweetify

from .models import SiteDetail, TeamMember, Subject
from .forms import MessageForm


class AboutPageView(View):
    def get(self, request):
        return render(request, "general/about.html")


class ContactPageView(View):
    def get(self, request):
        members = TeamMember.objects.all()

        form = MessageForm()

        context = {"members": members, "form": form}
        return render(request, "general/contact.html", context)

    def post(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(
                request,
                title="sent",
                text="Your Message was sent successfully",
                timer=3000,
            )
            return redirect("contact")

        context = {"form": form}
        return render(request, "general/contact.html", context)

