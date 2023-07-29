from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register_form/', views.registration, name='register_form'),
    path('logout/', views.logout_view, name='logout'),
    # path('login_form/', views.login_form, name='login_form'),
    # path('identity/', views.identity, name='identity'),
    # path('bethistory/', views.bethistory, name='bethistory'),
    # path('formTopMatch/', views.TopMatchForm, name='formTopMatch'),
    # path('formNextToGo/', views.NextToGoForm, name='formNextToGo'),
    # path('formTrending/', views.TrendingForm, name='formTrending'),
    # path('formUser/', views.UserForm, name='formUser'),
    # path('userAdmin/', views.UserAdmin, name='userAdmin'),
]