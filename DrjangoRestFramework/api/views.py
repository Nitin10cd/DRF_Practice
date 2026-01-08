from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def studentViews(request):
    students = {
        'id': 1,
        'name': 'Nitin Saxena',
        'class': 'Computer Science & Engineering'
    }
    return JsonResponse(students)