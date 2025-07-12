from django.db import models
from core_admin.models import User

class Teacher(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    fullname = models.CharField(max_length=255, null=True, blank=True)
    telegram_id = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )

    class Meta:
        db_table = "teachers"
        
    def __str__(self):
        return self.fullname if self.fullname else self.telegram_id