from django.shortcuts import render, redirect
from django.views import View

from .models import (
    SiteDetail, 
    TeamMember, 
    Subject
)
from  .forms import MessageForm


class AboutPageView(View):
    def get(self, request):
        sitedetail, created = SiteDetail.objects.get_or_create()

        context = {
            "site":sitedetail, 
                   }
        return render(request, 'general/about.html', context)


class ContactPageView(View):
    def get(self, request):
        members = TeamMember.objects.all()
        site, created = SiteDetail.objects.get_or_create()
        
        form = MessageForm()

        context = {
            "members":members,
            "site":site,
            "form":form
        }
        return render(request, "general/contact.html", context)
    
    def post(self, request):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')

        context = {
            "form":form
        }
        return render(request, "general/contact.html", context)
    