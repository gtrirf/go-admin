from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "fullname", "telegram_id", "user")
    search_fields = ("fullname", "telegram_id")