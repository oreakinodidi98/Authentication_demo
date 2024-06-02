from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User, Group
from .forms import RegisterForm

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            password_conf = form.cleaned_data['password_conf']
            if password == password_conf:
                new_user = User()
                new_user.username = form.cleaned_data['username']
                new_user.set_password(password)
                new_user.save()
                # add user to group
                if request.POST['account_type'] == 'poster':
                    # get the group
                    group = Group.objects.get(name='Posters')
                    # add user to group
                elif request.POST['account_type'] == 'reader':
                    group = Group.objects.get(name='Readers')
                # add user to group
                new_user.groups.add(group)
                login(request, new_user)
                return redirect('login')
    form = RegisterForm()
    return render(request, 'registration/register.html', context={'form':form})


def logout_user(request):
    logout(request)
    return redirect('login')