from django.contrib.auth import authenticate, login, logout
from .models import User, deserialize_user
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

# fix token authentication


class UserView(APIView):
    permission_classes = (permissions.AllowAny,)

    # remember to delete this function or use t for only your accounts..
    # u do not want bad actors to have access to this

    def get(self, request, format=None):
        """'
        Get the list of users make this have token uth and persmisson also
        Delete this func later please ....
        """
        users_list = []
        for user in User.objects.all():
            deserialized = deserialize_user(user)
            users_list.append(deserialized)
        return Response({
            'user_list': users_list
        })

    def post(self, request, format=None):
        """'
        create a user or something like that ...

        NOTES: Make email small letter
            Make first and last name accessible
        """
        ModelUser = get_user_model()
        if request.data:
            data = request.data
            email = data.get('email')
            email = email.lower()
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            password = data.get('password')
            is_student = data.get('is_student')
            is_tutor = data.get('is_tutor')
            user = ModelUser.objects.create_user(username=email, password=password, email=email,
                                                 last_name=last_name, first_name=first_name,
                                                 is_student=is_student, is_tutor=is_tutor)
            user.is_active = True
            user.save()
            return Response({
                'messages': 'success',
            })
        return Response({
            "message": 'fail'
        })


class UserNameChecker(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        """
        :return true or false based on the existence of a username
        """
        ModelUser = get_user_model()
        if request.data:
            username = request.data.get('username')
            username = username.lower()
            # check if it already exists .....
            username_query_set = ModelUser.objects.filter(username=username)
            if not username_query_set:
                return Response({
                    'exists': False,
                })
            else:
                return Response({
                    'exists': True,
                })


class UserDetailView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

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


# get rid of the user login view and the user logout view .... irrelevant
# enjoy

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
    permission_classes = (permissions.IsAuthenticated,)

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
