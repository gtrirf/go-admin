from django.db import models
from groups.models import Group


class Student(models.Model):
    id = models.PositiveIntegerField(primary_key=True)  # uint32 math with golang?
    fullname = models.CharField(max_length=255, null=True, blank=True)  # *string
    telegram_id = models.CharField(max_length=255, null=True, blank=True)  # *string
    group_id = models.PositiveSmallIntegerField(null=True, blank=True)  # *uint8
    phone_number = models.CharField(max_length=15, null=True, blank=True)  # *string
    is_active = models.BooleanField(default=False)
    age = models.PositiveSmallIntegerField(null=True, blank=True)  # *uint8
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'students'  # Exact table name

    def __str__(self):
        return self.fullname or f"Student #{self.phone_number}"


class StudentCode(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)  # uint8
    code = models.CharField(max_length=6, unique=True)
    student_id = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'student_codes'  # Exact table name
    
    def __str__(self):
        return self.code