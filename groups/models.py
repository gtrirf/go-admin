from django.db import models
from teacher.models import Teacher

class Group(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)  
    group_name = models.CharField(max_length=255, null=True, blank=True)
    time = models.TimeField()
    duration_hour = models.PositiveSmallIntegerField(null=True, blank=True)
    week_day = models.CharField(max_length=15)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return self.group_name or f"Group #{self.id}"
