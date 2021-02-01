from django.db.models.signals import post_save
from django.dispatch import receiver
from user_profiles.models import Student, Tutor, Schools
from users.models import User
from django.contrib.auth import get_user_model
# from .models import User
# from django.contrib.auth.models import User

# get instance of the school
_sch = Schools.objects.first()


@receiver(post_save, sender=User)
def create_profiles(sender, instance, created, **kwargs):
    if created:
        if instance.is_student is True:
            Student.objects.create(user=instance, school=_sch)
        if instance.is_tutor is True:
            Tutor.objects.create(user=instance, school=_sch)


@receiver(post_save, sender=User)
def save_profiles(sender, instance, **kwargs):
    if instance.is_student:
        instance.student.save()
    if instance.is_tutor:
        instance.tutor.save()
