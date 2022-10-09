from django.contrib import admin
from django.urls import path, include
from .views import (
    get_all_student,
    get_student_by_id,
    create_student,
    base,
    enter
)


urlpatterns = [
    path('', base),
    path('students/', get_all_student),
    path('student/<int:id>', get_student_by_id),
    path('student/create/', create_student)
]
