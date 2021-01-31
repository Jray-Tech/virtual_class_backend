from django.contrib.auth import authenticate, login, logout
from .models import User, Student, deserialize_user
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model


# come back and create the class for details and all ...and for updating user
# create the class to log users in and out
# return the shit for logged in usr .....type of user and stuff like that
# fix token authentication
# use json to do this .......or something sha

class UserView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        ''''
        Get the list of users make this have token uth and persmisson also
        '''
        users_list = []
        for user in User.objects.all():
            deserialized = deserialize_user(user)
            users_list.append(deserialized)
        return Response({
            'user_list': users_list
        })

    def post(self, request, format=None):
        ''''
        create a user or something like that ...
        '''
        ModelUser = get_user_model()
        if request.data:
            data = request.data
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
            is_student = data.get('is_student')
            is_tutor = data.get('is_tutor')
            user = ModelUser.objects.create_user(username=username, password=password, email=email,
                                                 is_student=is_student,
                                                 is_tutor=is_tutor)
            user.is_active = True
            user.save()
            return Response({
                'messages': 'success',
            })
        return Response({
            "message": 'fail'
        })


class UserDetailView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, pk):
        ''''
        Returns individual user
        '''
        try:
            user = User.objects.get(pk=pk)
            deserialized = deserialize_user(user)
            return Response({
                'user': deserialized
            })
        except User.DoesNotExist:
            return Response({
                "message":  'THE USER DOES NOT EXIST'
            })

    def post(self, request, format=None):
        ''''
        Allows you to update the user or something...dont forget to come back for it
        '''
        pass


class UserLogIn(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        ''''
        Chekc if user is authrnticated and logs user in ... with django . ill change it to token auth later
        '''
        if request.data:
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                de = deserialize_user(user)
                login(request, user)
                return Response({
                    'message': 'SUCCESS',
                    'user': de
                })


class UserLogOut(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        '''
        :param request:
        :return:
        Log user out
        '''
        logout(request)
        return Response({
            'message': 'SUCCESS'
        })
