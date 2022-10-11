from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView

from .models import Students, Group
from .forms import StudentsForm


class StudentsListView(ListView):
    model = Students
    template_name = 'students.html'


class Student(DetailView):
    model = Students
    template_name = 'student.html'
    queryset = Students.objects


def create_student(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
    form = StudentsForm()
    return render(request, 'dashboard.html', {'form': form})


def create_group(request):
    if request.method == 'POST':
        group = Group(name=request['name'])
        group.save()
        return


def base(request):
    return render(request, 'base.html')
