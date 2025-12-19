from django.http import HttpResponse #send simple text/html responses from a Django view.
from django.http import JsonResponse #Used to send JSON data from a Django view (good for APIs).
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Student2


# Create your views here.

def hello(request):
    return HttpResponse("Hello, World!")


def bye(request):
    return HttpResponse("Bye ")    


@csrf_exempt
def echo(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST only'}, status=405)
    data = json.loads(request.body or '{}')
    return JsonResponse({'received': data}, status=201)

@csrf_exempt
def update_echo(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body or '{}')
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        return JsonResponse({'action': 'updated', 'received': data}, status=200)
    return JsonResponse({'error': 'PUT only'}, status=405)

@csrf_exempt
def delete_echo(request):
    if request.method == 'DEL[ETE':
        # Return a JSON response with your custom message
        return JsonResponse({'status': 'deleted', 'user': 'nitesh'}, status=200)
    return JsonResponse({'error': 'DELETE only'}, status=405)


@method_decorator(csrf_exempt, name='dispatch')
class SimplePostView(View):
    def post(self, request):
        data = json.loads(request.body or '{}')
        # Return the received data'
        return JsonResponse({'received': data})


    def get(self, request):
        #data = json.loads(request.body or '{}')
        # Return the received data
        return JsonResponse({'received': "get"})

class UserAPI(APIView):
    def post(self, request):
        return Response(request.data, status=201)


from rest_framework import viewsets
from .models import Student1
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student1.objects.all()
    serializer_class = StudentSerializer


def simple_page(request):
    # Data without model
    products = [
        {'name': 'Book', 'price': 299, 'description': 'A good book'},
        {'name': 'Pen', 'price': 19, 'description': 'Blue ink pen'},
    ]
    return render(request, 'products.html', {'products': products})


@csrf_exempt
def student_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        student = Student2.objects.create(
            name=data['name'],
            age=data['age']
        )
        return JsonResponse({'id': student.id, 'name': student.name, 'age': student.age}, status=201)
    
    elif request.method == 'GET':
        students = Student2.objects.all()
        students_data = [{'id': s.id, 'name': s.name, 'age': s.age} for s in students]
        return JsonResponse({'students': students_data})

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

def login_page(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)   # creates session
            return redirect("/myapp/home/")
    return render(request, "page.html")

def home(request):
    if not request.user.is_authenticated:
        return HttpResponse("Not logged in")
    return HttpResponse(f"Hello {request.user.username}")

from rest_framework.views import APIView
from rest_framework.response import Response

#class based session creation
class ProfileAPI(APIView):
    def get(self, request):
        return Response({"user": request.user.username})




