from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView, api_view,action
from rest_framework import mixins,generics
from api.pagination import MyPagination, myCursorPagination, myLimitoffsetPagination
from api.serializers import MarksSerialier, StudentSerializer
from students.models import Marks, Student
from rest_framework import viewsets
# Create your views here.
# def studentView(request):
#     students=Student.objects.all()
#     std=list(students.values())
#     return JsonResponse(std,safe=False)


#-------------------- function based api views------------------
# @api_view(['GET','POST'])
# def studentView(request):
#     if request.method=='GET':
#         students=Student.objects.all()
#         serializer=StudentSerializer(students,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     elif request.method=='POST':
#         serializer=StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def studentDetailsView(request,pk):
#     student=get_object_or_404(Student,pk=pk)
#     if request.method=='GET':
#         serializer=StudentSerializer(student)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     elif request.method=='PUT':
#         serializer=StudentSerializer(student,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif request.method=='DELETE':
#         student.delete()
#         return Response({'message':'deleted succesfully'},status=status.HTTP_204_NO_CONTENT)


#------------------ Class based api views-------------------------------
# class StudentsView(APIView):
#     def get(self,request):
#         students=Student.objects.all()
#         serializer=StudentSerializer(students,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     def post(self,request):
#         serializer=StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# class StudentsdetailsView(APIView):
#     def get_obj(self,pk):
#         return get_object_or_404(Student,pk=pk)
#     def get(self,request,pk):
#         student=self.get_obj(pk)
#         serializer=StudentSerializer(student)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     def put(self,request,pk):
#         student=self.get_obj(pk)
#         serializer=StudentSerializer(student,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,pk):
#         student=self.get_obj(pk)
#         student.delete()
#         return Response({'message':'DELETE SUCCESFUL'},status=status.HTTP_404_NOT_FOUND)

#---------------------- mixins --------------------
# class StudentsView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
    
# class StudentsdetailsView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     def get(self,request,pk):
#         return self.retrieve(request)
#     def put(self,request,pk):
#         return self.update(request)
#     def delete(self,request,pk):
#         return self.destroy(request)

#---------------------------Generics ----------------------------
# class StudentsView(generics.ListAPIView,generics.CreateAPIView):
#     # queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     def get_queryset(self):
#         queryset=Student.objects.all()
#         age=self.request.query_params.get('age')
#         if age:
#             queryset=queryset.filter(age__gte=40)
#         return queryset

# class StudentsdetailsView(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     lookup_field='pk'


#----------------viewsets--------------------------------
# class StudentViewset(viewsets.ViewSet):
#     def list(self,request):
#         students=Student.objects.all()
#         serializer=StudentSerializer(students,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     def create(self,request):
#         serializer=StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)
#     def retrieve(self,request,pk):
#         student=get_object_or_404(Student,pk=pk)
#         serializer=StudentSerializer(student)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     def update(self,request,pk):
#         student=get_object_or_404(Student,pk=pk)
#         serializer=StudentSerializer(student,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
        
#     def delete(self,request,pk):
#         student=get_object_or_404(Student,pk=pk)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class StudentViewset(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

#     @action(detail=False,methods=['get'])
#     def student_age(self,request):
#         students=Student.objects.filter(age__gte=40)
#         serializer=self.get_serializer(students,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)

class StudentsView(generics.ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    

class StudentMarks(generics.ListCreateAPIView):
    queryset=Marks.objects.all()
    serializer_class=MarksSerialier
    pagination_class=myCursorPagination
    