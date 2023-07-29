from django.shortcuts import render,redirect
from .models import *
from .forms import *
from Admin.forms import *
from Account.views import registration
from django.contrib.auth import logout
from Betting.settings import EMAIL_HOST_USER
from django.core.mail import send_mail, EmailMultiAlternatives
import random

rand_num = random.randint(10000, 99999)
m = 0

def homepage(request):
    m = rand_num
    
    context = {
        'top_match' : TopMatch.objects.all(),
        'next_to_go' :NextToGo.objects.all(),
        'trending' : Trending.objects.all(),
        'league' : League.objects.all(),
        'club' : Club.objects.all(),
        'rand_num': m,
    }
    return render(request, 'index.html', context)

# def send_email(request):
#     user = User.objects.get(user = request.user)
#     user_email = User.customuser.email
#     context = {

#     }
#     send_mail(
#                 'You have been assigned',
#                 f'You have been assigned to take {m}',
#                 EMAIL_HOST_USER,
#                 [user_email],
#                 fail_silently=False,
#             )
#     return render(request, 'index.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

def dashboard(request):
    context = {

    }
    return render(request, 'dashboard.html', context)
    
def identity(request):
    context = {

    }
    return render(request, 'identity.html', context)

def bethistory(request):
    context = {

    }
    return render(request, 'bethistory.html', context)

# def send_mail(
#     'You have placed your bet',
#     'Your ticket number is{registry.employee.customuser.first_name}
#     EMAIL_HOST_USER,
#     [user_email],
#     fail_silently=False,)
#         return redirect('index')

# def TopMatchForm(request):
#     form = createTopMatch(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#         form = createTopMatch()
#     context = {
#         'formTopMatch':form
#     }
#     return render(request, 'form.html', context)

# def NextToGoForm(request):
#     form = createNextToGo(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = createNextToGo()
#     context = {
#         'formNextToGo':form
#     }
#     return render(request, 'form.html', context)

# def TrendingForm(request):
#     form = createTrending(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = createTrending()
#     context = {
#         'formTrending':form
#     }
#     return render(request, 'form.html', context)

# def UserForm(request):
#     form = createUser(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = createUser()
#     context = {
#         'formUser':form
#     }
#     return render(request, 'formUser.html', context)

# def UserAdmin(request):
#     context = {
#         'next_to_go' :NextToGo.objects.all(),
#     }
#     return render(request, 'admin.html', context)