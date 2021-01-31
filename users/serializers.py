from abc import ABC

from rest_framework import serializers
from .models import User
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'is_student', 'is_tutor', 'is_admin')


class CustomRegisterUser(RegisterSerializer):
    is_student = serializers.BooleanField()
    is_admin = serializers.BooleanField()
    is_tutor = serializers.BooleanField()

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'is_student', 'is_tutor', 'is_admin')

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'is_student': self.validated_data.get('is_student', ''),
            'is_tutor': self.validated_data.get('is_tutor', ''),
            'is_admin': self.validated_data.get('is_admin', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.is_student = self.cleaned_data.get('is_student')
        user.is_tutor = self.cleaned_data.get('is_tutor')
        user.is_admin = self.cleaned_data.get('is_admin')
        user.save()
        adapter.save_user(request, user, self)
        return user
