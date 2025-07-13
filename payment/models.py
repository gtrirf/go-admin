from django.db import models
from student.models import Student

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    paid_at = models.DateField()
    valid_until = models.DateField()

    class Meta:
        db_table = 'payments'
        indexes = [
            # Talaba ID bo'yicha tez qidirish uchun
            models.Index(fields=['student_id'], name='idx_payment_student'),
            
            # To'lov sanasi bo'yicha indeks
            models.Index(fields=['paid_at'], name='idx_payment_paid_at'),
            
            # Amal qilish muddati bo'yicha indeks
            models.Index(fields=['valid_until'], name='idx_payment_valid_until'),
            
            # Talaba va to'lov sanasi kombinatsiyasi uchun kompozit indeks
            models.Index(fields=['student_id', 'paid_at'], name='idx_payment_student_paid'),
            
            # Amal qilish muddati va to'lov sanasi kombinatsiyasi
            models.Index(fields=['valid_until', 'paid_at'], name='idx_payment_dates'),
        ]
        ordering = ['-paid_at']  # Default tartiblash

    def __str__(self):
        return f"Payment #{self.id}"

class MonthlyFee(models.Model):
    id = models.AutoField(primary_key=True)  
    amount = models.PositiveIntegerField(
        verbose_name="To'lov miqdori",
        help_text="UZS da ifodalangan"
    )
    description = models.TextField(
        verbose_name="Tavsif",
        blank=True,
        db_index=False
    )

    class Meta:
        db_table = 'monthly_fees'
        verbose_name = "Oylik to'lov"
        verbose_name_plural = "Oylik to'lovlar"
        indexes = [
            models.Index(fields=['amount'], name='amount_idx'),
        ]

    def __str__(self):
        return f"{self.amount:,} uzs"

class StudentFee(models.Model):
    id = models.AutoField(primary_key=True) 
    student_id = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True) 
    monthly_fee_id = models.ForeignKey(MonthlyFee, on_delete=models.SET_NULL, null=True, blank=True) 

    class Meta:
        db_table = 'student_fees' 
    
    def __str__(self):
        return f'{self.monthly_fee_id.amount} for {self.student_id.fullname}'