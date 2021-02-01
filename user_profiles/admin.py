from django.contrib import admin
from .models import Schools, Student, Courses, Tutor
# Register your models here.
admin.site.register(Schools)
admin.site.register(Courses)
admin.site.register(Tutor)
admin.site.register(Student)


