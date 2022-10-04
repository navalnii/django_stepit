from django.shortcuts import render
from django.http import HttpResponse
from .models import Students, Group
from django.shortcuts import get_object_or_404
from django.http import Http404


# Create your views here.
def get_all_student(request):
    all_student = Students.objects.all()
    return HttpResponse(all_student)


def get_student_by_id(request, id):
    return get_object_or_404(Students, pk=id)


# def create_student(request):
#     if request.method == 'POST':
#         student = Students.objects.create(name=request['name'],
#                                           surname=request['surname'],
#                                           age=request['age'],
#
#                                           )

def create_group(request):
    if request.method == 'POST':
        group = Group(name=request['name'])
        group.save()
        return