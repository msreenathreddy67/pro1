from django.db import models

# Create your models here.


class School(models.Model):
    name=models.CharField(max_length=30)
    principal=models.CharField(max_length=20)
    loc=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.PositiveIntegerField() 
    school=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')


    def __str__(self):
        return self.name 