from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import SiteDetail, TeamMember, Subject, Message


class SiteDetailAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        obj, created = self.model.objects.get_or_create() 

        return HttpResponseRedirect(
            reverse(
                "admin:%s_%s_change"
                % (self.model._meta.app_label, self.model._meta.model_name),
                args=(obj.id,),
            )
        )
    
    def has_add_permission(self, request) :
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False



class MessageAdmin(admin.ModelAdmin):
    list_display = ["name", "subject", "created_at", "updated_at"]
    list_filter = list_display


admin.site.register(SiteDetail, SiteDetailAdmin)
admin.site.register(TeamMember)
admin.site.register(Subject)
admin.site.register(Message, MessageAdmin)

