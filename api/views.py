from rest_framework.decorators import api_view
from api import models, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import(
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView
)

class StudentListView(ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    permission_classes = [IsAuthenticated]

class StudentDetailsView(RetrieveUpdateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    permission_classes = [IsAuthenticated]

class StudentDeleteView(DestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

























#from django.http import HttpResponse
#import json

#from django.shortcuts import render



# Create your views here.

# class Student:
#     name = "rohan"
#     roll = 22
#     marks = 129

# @api_view()
# def usersApi(request):
    
#     student = Student()
#     response = serializers.StudentSerializer(student)

#     return Response(response.data)

# # dumps will take in any python object and will serialize it into json string
 
#  #converting python objects to json format is called serialization# users = [
#     #     {
#     #         "name": "Jatin katyal",
#     #         "languages" : "python"
#     #     },
#     #     {
#     #         "name": "Chris",
#     #         "languages" : "c++"
#     #     }
#     # ]