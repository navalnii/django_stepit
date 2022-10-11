from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Students(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"Name: {self.name} {self.surname}"


class StudentsGroup(models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)


class Teachers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)


class Scores(models.Model):
    students_group_id = models.ForeignKey(StudentsGroup, on_delete=models.CASCADE)
