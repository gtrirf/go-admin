from django.contrib import admin
from .models import Student, StudentCode

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'phone_number', 'telegram_id', 'get_group', 'is_active', "age")
    list_filter = ('is_active', )

    def get_group(self, obj):
        return obj.group.group_name if obj.group else "-"
    get_group.short_description = 'Group'
    
@admin.register(StudentCode)
class StudentCodeAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "get_student", "is_active", "created_at")
    search_fields = ("code",)

    def get_student(self, obj):
        return obj.student.fullname
    get_student.short_description = 'Student'