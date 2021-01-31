from django.urls import include, path
from rest_framework import routers
from . import views


urlpatterns = [
    path('',  views.UserView.as_view(), name='userView'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='userDetails'),
    path('logout/', views.UserLogOut.as_view(), name='userLogOutView'),
    path('login/', views.UserLogIn.as_view(), name='userLogInView'),
]