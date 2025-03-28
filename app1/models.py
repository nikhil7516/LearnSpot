# Create your models here.
from django.db import models

class tbl_Course(models.Model):
    title=models.CharField(max_length=500)
    description=models.CharField(max_length=10000)
    Course=models.CharField(max_length=500)
    class meta:
        db_table="tbl_course"
        