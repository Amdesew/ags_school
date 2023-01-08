from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    grade = models.CharField(max_length=6)
    student_id = models.FloatField(max_length=20)
    test_one = models.TextField()
    test_two = models.TextField()
    mid_exam = models.TextField()
    test_three = models.TextField()
    final_exam = models.TextField()