from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group


admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "phone_number", "username", "role", "is_active", "is_staff")
    search_fields = ("phone_number", "username")
    list_filter = ("role", "is_active")