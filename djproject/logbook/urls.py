from django.contrib import admin
from django.urls import path, include
from .views import (
    Student,
    create_student,
    base,
    StudentsListView
)


urlpatterns = [
    path('', base),
    path('students/', StudentsListView.as_view()),
    path('student/<int:pk>', Student.as_view()),
    path('student/create/', create_student),
]
