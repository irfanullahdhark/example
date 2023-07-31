from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework.views import APIView


# @api_view()
# def hello(request):
#     return Response({'msg':'hello world'})


# using third party myapp application api
# @api_view(['GET','POST','PUT','DELETE'])
# def hello(request):
#     if request.method == 'GET':
#         id = request.data.get('id',None)
#         if id is not None:
#             stu = Student.objects.get(pk=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         all = Student.objects.all()
#         serializer = StudentSerializer(all,many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'data created!'}
#             return Response(res)
#         return Response(serializer.errors)
#
#     if request.method == "PUT":
#         id = request.data.get('id')
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'data updated!'})
#         return Response(serializer.errors)
#
#     if request.method == "DELETE":
#         id = request.data.get('id')
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'data deleted!'})


# using browsable api

class StudentApi(APIView):
    def get(self,request,pk=None, format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        all = Student.objects.all()
        serializer = StudentSerializer(all,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created!'}
            return Response(res)
        return Response(serializer.errors)

    def put(self,request,pk=None,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data Compete updated!'})
        return Response(serializer.errors)

    def patch(self,request,pk=None,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data Partially updated!'})
        return Response(serializer.errors)

    def delete(self,request,pk=None,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'data deleted!'})


# using browsable api
# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# def hello(request,pk=None):
#     if request.method == 'GET':
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(pk=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         all = Student.objects.all()
#         serializer = StudentSerializer(all,many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'data created!'}
#             return Response(res)
#         return Response(serializer.errors)
#
#     if request.method == "PUT":
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'data Compete updated!'})
#         return Response(serializer.errors)
#
#     if request.method == "PATCH":
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'data Partially updated!'})
#         return Response(serializer.errors)
#
#     if request.method == "DELETE":
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'data deleted!'})



