from django.db import models
from student.models import Student
from groups.models import Group

class Attendance(models.Model):
    id = models.AutoField(primary_key=True)  # uint8
    student_id = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True) 
    group_id = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    present = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'attendances'

    def __str__(self):
        return f"{self.student_id.fullname} {f"{self.present} keldi" if self.present else f"{self.date} kelmadi"}"
    
class Location(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)  
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()

    class Meta:
        db_table = 'locations'  # Exact table name

    def __str__(self):
        return self.description