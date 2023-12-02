from django.db import models

# Create your models here.

class student_basic(models.Model):
    F_name=models.CharField(max_length=20)
    L_name=models.CharField(max_length=20)
    Registration_no=models.IntegerField(primary_key=True)

    def __str__(self) -> str:
        return self.F_name