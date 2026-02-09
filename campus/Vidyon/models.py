from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    course = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


# ---------- Academics ----------

class Admission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.student.name


class Test(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    marks = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.student.name


class Fees(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    total_fees = models.IntegerField()
    paid = models.IntegerField()
    balance = models.IntegerField()

    def __str__(self):
        return self.student.name


# ---------- Activities ----------

class Activity(models.Model):
    CATEGORY = (
        ('Sports', 'Sports'),
        ('Cultural', 'Cultural'),
        ('Competition', 'Competition'),
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY)
    date = models.DateField()
    winner = models.CharField(max_length=100)

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username
