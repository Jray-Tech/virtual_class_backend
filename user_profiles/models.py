from django.db import models
from users.models import User
# Create your models here.
#
# tutor rating ....


def deserialize_school(sch):
    return {
        'name': sch.name
    }


def deserialize_course(crs):
    return {
        'name': crs.name
    }


def deserialize_student(std):
    user = std.user.id
    profile_picture = std.profile_picture.url
    bio = std.bio
    school = deserialize_school(std.school)
    courses = []
    for course in std.courses.all():
        deserialized_course = deserialize_course(course)
        courses.append(deserialized_course)
    return {
        'user_id': user,
        'profile_picture': profile_picture,
        'bio': bio,
        'school': school,
        'courses': courses
    }


def deserialize_tutor(tur):
    user = tur.user.id
    profile_picture = tur.profile_picture.url
    bio = tur.bio
    school = deserialize_school(tur.school)
    courses = []
    for course in tur.teach_courses.all():
        deserialized_course = deserialize_course(course)
        courses.append(deserialized_course)
    return {
        'user_id': user,
        'profile_picture': profile_picture,
        'bio': bio,
        'school': school,
        'courses': courses
    }


class Schools(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Courses(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=800, blank=True)
    # school
    school = models.ForeignKey(Schools, on_delete=models.DO_NOTHING, blank=True)
    courses = models.ManyToManyField(Courses, blank=True)

    def __str__(self):
        return f'{self.user.username} student profile'

# when you want to make changes loook at the signals ...they are now linked ... consider that too


class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.jpeg', upload_to='profile_pics')
    bio = models.CharField(max_length=800, blank=True)
    school = models.ForeignKey(Schools, on_delete=models.DO_NOTHING)
    teach_courses = models.ManyToManyField(Courses, blank=True)
    # courses_can_teach

    def __str__(self):
        return f'{self.user.username} tutor profile'




