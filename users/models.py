from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here
# toekn = 0764ea43a17b4d7517aa061d8e1579248ca50b2c


def deserialize_user(user):
    user_json = {
        'username': user.username,
        'email': user.email,
        'is_student': user.is_student,
        'is_tutor': user.is_tutor,
        'id': user.id,
    }
    return user_json


class User(AbstractUser):
    is_student = models.BooleanField()
    is_tutor = models.BooleanField()

    def __str__(self):
        return self.username

#
# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.user.username

