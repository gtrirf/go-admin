from django.db import models
from student.models import Student

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True) 
    paid_at = models.DateField()
    valid_until = models.DateField()

    class Meta:
        db_table = 'payments'  # Exact table name

    def __str__(self):
        return f"Payment #{self.id}"

class MonthlyFee(models.Model):
    id = models.AutoField(primary_key=True)  
    amount = models.PositiveIntegerField()
    description = models.TextField()

    class Meta:
        db_table = 'monthly_fees'  # Exact table name

    def __str__(self):
        return f"{self.amount} uzs"

class StudentFee(models.Model):
    id = models.AutoField(primary_key=True) 
    student_id = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True) 
    monthly_fee_id = models.ForeignKey(MonthlyFee, on_delete=models.SET_NULL, null=True, blank=True) 

    class Meta:
        db_table = 'student_fees' 
    
    def __str__(self):
        return f'{self.monthly_fee_id.amount} for {self.student_id.fullname}'