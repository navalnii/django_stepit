from django.db import models


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=20)


class Students(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)


class StudentsGroup(models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)


class Teachers(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)


class Scores(models.Model):
    students_group_id = models.ForeignKey(StudentsGroup, on_delete=models.CASCADE)
