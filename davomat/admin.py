from django.contrib import admin
from .models import Attendance, Location

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_student', 'get_group', 'date', 'present')

    def get_student(self, obj):
        return obj.student.fullname
    get_student.short_description = 'Student'

    def get_group(self, obj):
        return obj.group.group_name
    get_group.short_description = 'Group'

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "latitude", "longitude")