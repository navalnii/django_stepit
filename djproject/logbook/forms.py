from django import forms
from django.contrib.auth.models import User

from .models import Teachers


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class TeachersForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = ('name', 'surname', 'group_id')

