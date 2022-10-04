from django.contrib import admin
from django.urls import path, include
from .views import get_all_student, get_student_by_id


urlpatterns = [
    path('students/', get_all_student),
    path('student/<int:id>', get_student_by_id),

]
