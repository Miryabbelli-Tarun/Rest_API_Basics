from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.serializers import StudentSerializer
from students.models import Student
# Create your views here.
# def studentView(request):
#     students=Student.objects.all()
#     std=list(students.values())
#     return JsonResponse(std,safe=False)

@api_view(['GET','POST'])
def studentView(request):
    if request.method=='GET':
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def studentDetailsView(request,pk):
    student=get_object_or_404(Student,pk=pk)
    if request.method=='GET':
        serializer=StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        student.delete()
        return Response({'message':'deleted succesfully'},status=status.HTTP_204_NO_CONTENT)