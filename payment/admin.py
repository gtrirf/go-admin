from django.contrib import admin
from .models import Payment, StudentFee, MonthlyFee

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_student', 'paid_at', 'valid_until')

    def get_student(self, obj):
        return obj.student.fullname if obj.student else "-"
    get_student.short_description = 'Student'

@admin.register(MonthlyFee)
class MonthlyFeeAdmin(admin.ModelAdmin):
    list_display = ("id", "amount", "description")

@admin.register(StudentFee)
class StudentFeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_student', 'get_monthly_fee')

    def get_student(self, obj):
        return obj.student.fullname if obj.student else "-"
    def get_monthly_fee(self, obj):
        return obj.monthly_fee.amount if obj.monthly_fee else "-"
    get_student.short_description = 'Student'
    get_monthly_fee.short_description = 'Monthly Fee'
