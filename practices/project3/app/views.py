from .serializer import StudentSerializer
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Student
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    if request.method == "GET":
        json_data = request.body
        print(f'json data is {json_data}------------------------------------------------')
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu)
            return JsonResponse(serializer.data, safe=False)

        else:
            print('--------------------------------------------')
            all = Student.objects.all()
            serializer = StudentSerializer(all, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data saved'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')

        json_data = JSONRenderer.render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    if request.method == 'PUT':
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=python_data,partial=True)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'DELETE':
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()

        res = {'msg':'data deleted!'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')







