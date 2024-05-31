from django.contrib import admin
from django.utils import timezone
from .models import SupportMessage
from django.urls import path
from django.http import HttpResponseRedirect
from django.shortcuts import render


@admin.register(SupportMessage)
class SupportMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'replied', 'created_at', 'replied_at')
    search_fields = ('user__username', 'message', 'reply')
    actions = ['reply_to_messages']

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('reply/<int:message_id>/', self.admin_site.admin_view(self.reply_to_message), name='reply_to_message'),
        ]
        return custom_urls + urls

    def reply_to_message(self, request, message_id):
        message = self.get_object(request, message_id)
        if request.method == 'POST':
            reply = request.POST.get('reply')
            if reply:
                message.reply = reply
                message.replied = True
                message.replied_at = timezone.now()
                message.save()
                self.message_user(request, "Replied to support message.")
                return HttpResponseRedirect(f"/admin/diary/supportmessage/{message_id}/change/")
        return render(request, 'admin/reply_to_message.html', {'message': message})

    def reply_to_messages(self, request, queryset):
        if queryset.count() == 1:
            message = queryset.first()
            return HttpResponseRedirect(f"/admin/diary/supportmessage/reply/{message.pk}/")
        else:
            self.message_user(request, "Please select exactly one message to reply to.", level='error')

    reply_to_messages.short_description = "Reply to selected support messages"
