from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def students(request):
    students = [
        {'id': 1, 'name': 'Nitin Saxena', 'age': 20},
        {'id': 2, 'name': 'Shreya', 'age': 20},
    ]
    return HttpResponse(students)