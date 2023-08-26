from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator

# Create your models here.

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_modified_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
        

class User(AbstractUser):
    username = models.EmailField("Email", unique=True, validators=[EmailValidator])
    date_of_birth = models.DateField(null=True)
    date_of_registration = models.DateField(null=True)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username


class Lessons(models.Model):
    lesson_name = models.CharField(max_length=50)
    teacher = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='lesson_of_teacher')
    students = models.ManyToManyField(User, related_name='lesson_of_students', through='ExamGrade')
    
    term = models.DateField(null=True)
    
    def __str__(self):
        return self.lesson_name
    


class ExamGrade(BaseModel):
    student = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='student_grade')
    lesson = models.ForeignKey(Lessons, on_delete=models.DO_NOTHING, related_name='lesson')
    
    grade = models.IntegerField(null=True)
    date_of_exam = models.DateField(null=True)
    took_exam = models.BooleanField(default=True)
    
    def __str__(self):
        return self.student

