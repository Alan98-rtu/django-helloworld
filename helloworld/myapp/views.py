
from django.shortcuts import render

def hello_world(request):
    return render(request, 'hello.html', {'message': 'Hello, World!'})