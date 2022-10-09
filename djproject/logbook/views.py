from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import Http404, HttpResponseRedirect

from .models import Students, Group
from .forms import TeachersForm, UserForm


# Create your views here.
def get_all_student(request):
    all_student = Students.objects.all()
    return HttpResponse(all_student)


def get_student_by_id(request, id):
    return get_object_or_404(Students, pk=id)


def create_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
    form = StudentForm()
    return render(request, 'dashboard.html', {'form': form})


def create_group(request):
    if request.method == 'POST':
        group = Group(name=request['name'])
        group.save()
        return


def base(request):
    return render(request, 'base.html')


def enter(request):

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        render(request, '')
    else:
        # Return an 'invalid login' error message.
        render(request, 'error')

    # if request.user.is_authenticated:
    #     return redirect('/')
    # else:
    #     if request.method == 'POST':
    #         if 'signupform' in request.POST:
    #             signupform = TeachersForm(data=request.POST)
    #             signinform = TeachersForm()
    #
    #             if signupform.is_valid():
    #                 username = signupform.cleaned_data['username']
    #                 password = signupform.cleaned_data['password1']
    #                 signupform.save()
    #                 user = authenticate(username=username, password=password)
    #                 login(request, user)
    #                 return redirect('/')
    #
    #         else:
    #             signinform = TeachersForm(data=request.POST)
    #             signupform = TeachersForm()
    #
    #             if signinform.is_valid():
    #                 login(request, signinform.get_user())
    #                 return redirect('/')
    #
    #     else:
    #         signupform = TeachersForm()
    #         signinform = TeachersForm()
    #
    # return render(request, 'enter.html', {'signupform': signupform,
    #                                       'signinform': signinform})


class TeacherUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = TeachersForm
    template_name = 'enter.html'

    def post(self, request):

        post_data = request.POST or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = TeachersForm(post_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, 'Your profile was successfully updated!')
            return HttpResponseRedirect('profile')

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
