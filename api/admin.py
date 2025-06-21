from django.contrib import admin
from django.contrib.auth.models import User
from .models import EmailLog

# Unregister the default User admin
admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Customized admin for the built-in User model.
    """
    list_display = ['username', 'email', 'is_staff', 'date_joined']
    search_fields = ['username', 'email']
    list_filter = ['is_staff', 'date_joined']
    ordering = ['-date_joined']

@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    """
    Admin view for email log entries.
    """
    list_display = ['username', 'email', 'sent_at']
    search_fields = ['username', 'email']
    list_filter = ['sent_at']
    ordering = ['-sent_at']
