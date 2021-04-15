from django.shortcuts import render
from .models import Schools, Courses, Student, Tutor, deserialize_student, deserialize_tutor, deserialize_course
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView




# api does the following
# update profile
# delete profile
# list and details for the students and the tutors ...
# get students and tutors based on specific things ..... filters and search based on what you need
# use one for an example .... give use name and check the diff lookup params and give
# ........do any other thing lol
# ......create courses ...for tutors not these guys so not here in classroom meaintaninance


# post list gives based on reasons ....get gives paginated list of the shit or maybe all of them for now
# and lets you kmnow how many they are ....sounds hard so i might skip it for now

# send ur student id when it is created ....it will be created with a signal
# POSSIBLE ERRORS IN POST METHOD ...IF USER TRIES TO GET COURSES THAT  DONT EXIST WE ARENT TAKING CARE OF THAT
class StudentListView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        """'
        Get list of students
        """
        student_list = []
        for std in Student.objects.all():
            deserialized = deserialize_student(std)
            student_list.append(deserialized)
        return Response({
            'student_list': student_list,
        })

    def post(self, request):
        """'
        Gives us data based on reasons different reason for diff uses
        Story sha but it is good for us to use
        ...for example --> API, with reverse lookup.. based on
            -> courses studied
            -> time ? .. .
            -> name
            -> ...keep it simple then come back to add more complex functionality.

            -> I am too tired to test this code i hope it works
        """
        data = request.data
        if data:
            search = data.get('search')
            courses_studied = data.get('courses_studied')
            if courses_studied is not None:
                courses = []
                for c in courses_studied:
                    _c = Courses.objects.get(pk=c)
                    courses.append(_c)
                    # now  we have a list of course objects... called courses
                std_returned = []
                # now that i have all courses ...get  a list of students doing a course or multiple courses..
                # enjoy!  ..... Make sure courses do not overlap or so

                for course in courses:
                    s = Student.objects.filter(courses=course)
                    for item in s:
                        if item not in std_returned:
                            std_returned.append(item)
                # now i have a list of objects ill convert to JSON
                # TURN COURSE INTO COURSE OBJECTS!!!!!
                cleaned_student = []
                for obj in std_returned:
                    _obj = deserialize_student(obj)
                    cleaned_student.append(_obj)
                return Response({
                    'student_list': cleaned_student
                })

# student detail and update
# tutors version
# get urls
# test code...


class StudentDetailView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk):
        """"
        Get the student detail by looking up its shit
        """
        try:
            student = Student.objects.get(pk=pk)
            deserialized = deserialize_student(student)
            return Response({
                'student': deserialized
            })
        except Student.DoesNotExist:
            return Response({
                "message":  'THE USER DOES NOT EXIST'
            })

    def post(self, request, pk):
        """'
        Add to the code
            -> Update or delete things from the dastabase
            -> just get what is given and update profile accordingly
        """
        data = request.data
        try:
            a = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({
                'message': 'Does not exist sorry guy'
            })
        if data:
            profile_picture = data.get('profile_picture')
            bio = data.get('bio')
            courses_id_list = data.get('courses_id_list')
            school = data.get('school')
            if bio is not None:
                # access user model from token during production
                bio = str(bio)
                a.bio = bio
                a.save()
                # come back and figure out how to save files nd send them
            if school is not None:
                school_obj = Schools.objects.get(pk=school)
                a.school = school_obj
                a.save()
            if courses_id_list is not None:
                for course_id in courses_id_list:
                    _course = Courses.objects.get(id=course_id)
                    a.courses.add(_course)
                    a.save()
            return Response({
                'message': 'SUCCESS',
                'student': deserialize_student(a)
            })
        return  Response({
            'message': 'FAILED O'
        })


class TutorsListView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        """'
        Get list of tutors.. .For Your Consideration
        """
        tutor_list = []
        for tur in Tutor.objects.all():
            deserialized = deserialize_tutor(tur)
            tutor_list.append(deserialized)
        return Response({
            'tutor_list': tutor_list,
        })

    def post(self, request):
        """'
        Gives us data based on reasons different reason for diff uses
        Story sha but it is good for us to use
        ...for example --> API, with reverse lookup.. based on
            -> courses studied will return the students or tutors doing the course
            -> time ? .. .
            -> name
            -> ...keep it simple then come back to add more complex functionality.

            -> I am too tired to test this code i hope it works
        """
        data = request.data
        if data:
            search = data.get('search')
            courses_studied = data.get('courses_studied')
            if courses_studied is not None:
                courses = []
                for c in courses_studied:
                    _c = Courses.objects.get(pk=c)
                    courses.append(_c)
                    # now  we have a list of course objects... called courses
                tur_returned = []
                # now that i have all courses ...get  a list of students doing a course or multiple courses..
                # enjoy!  ..... Make sure courses do not overlap or so
                for course in courses:
                    s = Tutor.objects.filter(courses=course)
                    for item in s:
                        if item not in tur_returned:
                            tur_returned.append(item)
                # now i have a list of objects ill convert to JSON
                # TURN COURSE INTO COURSE OBJECTS!!!!!
                cleaned_tutors = []
                for obj in tur_returned:
                    _obj = deserialize_student(obj)
                    cleaned_tutors.append(_obj)
                return Response({
                    'tutors_list': cleaned_tutors
                })

# student detail and update
# tutors version
# get urls
# test code...


class TutorDetailView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk):
        """"
        Get the student detail by looking up its shit
        """
        try:
            tutor = Tutor.objects.get(pk=pk)
            deserialized = deserialize_tutor(tutor)
            return Response({
                'tutor': deserialized
            })
        except Tutor.DoesNotExist:
            return Response({
                "message":  'THE USER DOES NOT EXIST'
            })

    def post(self, request, pk):
        """'
        Add to the code
            -> Update or delete things from the dastabase
            -> just get what is given and update profile accordingly
        """
        data = request.data
        try:
            a = Tutor.objects.get(pk=pk)
        except Tutor.DoesNotExist:
            return Response({
                'message': 'Does not exist sorry guy'
            })
        if data:
            profile_picture = data.get('profile_picture')
            bio = data.get('bio')
            courses_id_list = data.get('courses_id_list')
            school = data.get('school')
            if bio is not None:
                # access user model from token during production
                bio = str(bio)
                a.bio = bio
                a.save()
                # come back and figure out how to save files nd send them
            if school is not None:
                school_obj = Schools.objects.get(pk=school)
                a.school = school_obj
                a.save()
            if courses_id_list is not None:
                for course_id in courses_id_list:
                    _course = Courses.objects.get(id=course_id)
                    a.courses.add(_course)
                    a.save()
            return Response({
                'message': 'SUCCESS',
                'tutor': deserialize_tutor(a)
            })
        return  Response({
            'message': 'FAILED O, I no know why oooo .....sorry bor!'
        })


# other api come and add them here as needed ..
# the basic functionality is set!
# next add signals to update as it starts
# do media changes and urls ......set media to change profile pics
# don't be too worried about whr images will be stored ....code will still work regardless .
