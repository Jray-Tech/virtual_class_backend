from django.urls import include, path
from rest_framework import routers
from . import views


urlpatterns = [
    path('students/',  views.StudentListView.as_view(), name='studentListView'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='studentDetailView'),
    path('tutors/', views.TutorsListView.as_view(), name='tutorListView'),
    path('tutors/<int:pk>/', views.TutorDetailView.as_view(), name='tutorDetailView'),
]