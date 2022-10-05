from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import Http404

from .models import Students, Group
from .forms import StudentForm


# Create your views here.
def get_all_student(request):
    all_student = Students.objects.all()
    return HttpResponse(all_student)


def get_student_by_id(request, id):
    return get_object_or_404(Students, pk=id)


def create_student(request):
    form = StudentForm(request.POST)
    if form.is_valid():
        try:
            st = Students.objects.create(
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                age=form.cleaned_data['age']
            )
            return get_object_or_404(st)
        except:  # duplicate email
            pass


def create_group(request):
    if request.method == 'POST':
        group = Group(name=request['name'])
        group.save()
        return
