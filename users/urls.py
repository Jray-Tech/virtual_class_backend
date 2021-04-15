from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('create/',  views.UserView.as_view(), name='userView'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='userDetails'),
    path('exists/', views.UserNameChecker.as_view(), name='usernameChecker'),
    path('api-token-auth/', obtain_auth_token, name='auth_token_api'),

    path('logout/', views.UserLogOut.as_view(), name='userLogOutView'),
    path('login/', views.UserLogIn.as_view(), name='userLogInView'),
]