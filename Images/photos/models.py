from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        (1, 'Hod'),
        (2, 'student'),
        (3, 'teacher')

    )
    user_type = models.CharField(choices=USER,max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')


class Admin (models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    objects = models.Manager()

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    address = models.TextField()
    objects = models.Manager()

class teacher_images(models.Model):
    image_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/')
    objects = models.Manager()






class sign_up(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=300)


    number = models.BigIntegerField()

    def __str__(self):
        return self.name

class student_images(models.Model):
    image_id = models.ForeignKey(sign_up, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/')
    objects = models.Manager()