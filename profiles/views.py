from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from .models import Profile

from .forms import ProfileForm


def register_view(request):
    """
    Register View
    :param request:
    :return:
    """
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        new_user = User.objects.create_user(username=username, email=email, password=password2)
        new_user.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'profiles/register.html')


def login_view(request):
    """
    Login View
    :param request:
    :return:
    """
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            home_page = get_object_or_404(Profile,  user=user).home_page
            if home_page:
                return HttpResponseRedirect(home_page)
            else:
                return HttpResponseRedirect('/')
        else:
            message = 'Invalid login credentials'
            html = '<div class="alert alert-warning" role="alert"><i class="fa fa-fw text-danger m-r-1"></i>{}.</div>'.format(
                message)
            return render(request, 'profiles/login.html', {'message': message})
    else:
        return render(request, 'profiles/login.html')


def logout_view(request):
    """
    Logout View
    :param request:
    :return:
    """
    auth.logout(request)
    return HttpResponseRedirect('/')


def profile_view(request):
    """
    Profile details view
    :param request:
    :return:
    """
    profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
    if request.method == 'POST':
        if profile_form.is_valid():
            profile_form.save()
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html',  {'profile_form': profile_form})


def other_profile_view(request, profile_id):
    """
    Other Profile details view
    :param request:
    :return:
    """
    return render(request, 'profiles/profile.html')
