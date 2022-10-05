from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    surname = forms.CharField(label='Your surname', max_length=100)
    age = forms.IntegerField(label='Your age', max_length=100)
