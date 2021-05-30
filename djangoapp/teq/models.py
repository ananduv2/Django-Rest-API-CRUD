from django.db import models

# Student Model.
class Students(models.Model):
    StudentId=models.AutoField(primary_key=True)
    StudentName=models.CharField(max_length=100)
    StudentMob=models.CharField(max_length=10)
    StudentEmail=models.EmailField(max_length=100)
    class Meta:
        db_table="students"
    def __str__(self):
        return self.StudentName

# Course Model.
class Courses(models.Model):
    CourseId=models.AutoField(primary_key=True)
    CourseName=models.CharField(max_length=100)
    CourseRate=models.IntegerField()
    class Meta:
        db_table="courses"
    def __str__(self):
        return self.CourseName
