from django.contrib import admin
from .models import Group

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'group_name', 'time', 'duration_hour', 'get_teacher')

    def get_teacher(self, obj):
        return obj.teacher.fullname if obj.teacher else "-"
    get_teacher.short_description = 'Teacher'
