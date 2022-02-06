from django.shortcuts import render
from rest_framework import viewsets,permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilalizers import Studentserializers
from django.contrib.auth.models import User
from django.http import HttpResponse
from affairs.models import Students


# Create your views here.



class Studentlist(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = Studentserializers
    permission_classes = [permissions.IsAuthenticated]

@api_view(['delete','get'])
def deleteStudent(request,id):
    Students.objects.filter(id=id).delete()
    return Response({'Status': 'Student Deleted'})

@api_view(['post'])
def updateStudent(request,id):
    name = request.GET['name']
    email = request.GET['email']
    Students.objects.filter(id=id).update(name=name,email=email)
    return Response({'Status': 'Student Updated'})
