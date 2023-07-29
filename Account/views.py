from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


# Create your views here.
def registration(request):
    msg = 'None'

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'user created'
            return redirect('/login_form')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'register_form.html', {'form' : form, 'msg' : msg})

# def login_view(request):
#     form = LoginForm(request.POST or None)
#     msg = None
#     if request.method == 'POST':
#         if form.is_valid():
#             email = form.cleaned_data.get('Email')
#             password = form.cleaned_data.get('Password')
#             user = authenticate(email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('/index1')
#             else:
#                 msg = 'invalid credentials'
#         else:
#             msg = 'error validating form'
#     return render(request, 'login_form.html', {'form' : form, 'msg' : msg})

def index1(request):
    return render(request, 'index1.html')





def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                    login(request, user)
                    return redirect('/')
            else:
                return render(request, 'login_form.html', {'form': form, 'error_message': 'Invalid login credentials'})
    else:
        form = LoginForm()
    return render(request, 'login_form.html', {'form': form})



def registration(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        employee_form = UserForm(request.POST, request.FILES)

        if user_form.is_valid() and employee_form.is_valid():
            user = user_form.save(commit=False)
            user.is_employee = True
            user.save()
            employee = employee_form.save(commit=False)
            employee.customuser = user
            employee.save()
            return redirect ('/user_login')
    else:
        user_form = CustomUserCreationForm()
        employee_form = UserForm()
    return render(request, 'register_form.html', {'user_form': user_form, 'employee_form': employee_form})