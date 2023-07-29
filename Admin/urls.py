from django.urls import path
from . import views

urlpatterns = [
    path('admin1/', views.homepage, name='index'),
    path('chart/', views.chart, name='chart'),
    path('basicElements/', views.basicElements, name='basicElements'),
    path('bootTable/', views.bootTable, name='bootTable'),
    path('calender/', views.calender, name='calender'),
    path('dataTable/', views.dataTable, name='dataTable'),
    path('dropdown/', views.dropdown, name='dropdown'),
    path('forgotPass/', views.forgotPass, name='forgotPass'),
    path('invoice/', views.invoice, name='invoice'),
    path('layouts/', views.layouts, name='layouts'),
    # path('login/', views.login_view, name='login'),
    path('register/', views.registration, name='register'),
    path('betSlip/<int:id>/', views.betSlip, name='betSlip'),

    # Admin
    path('newAdmin/', views.newAdmin, name='newAdmin'),
    path('adminList/', views.adminList, name='adminList'),
    path('deleteAdmin/<int:id>/', views.deleteAdmin, name='deleteAdmin'),
    path('editAdmin/<int:id>/', views.editAdmin, name='editAdmin'),

    # User
    path('newUser/', views.newUser, name='newUser'),
    path('userList/', views.userList, name='userList'),
    path('deleteUser/<int:id>/', views.deleteUser, name='deleteUser'),
    path('editUser/<int:id>/', views.editUser, name='editUser'),

    # League
    path('formLeague/', views.LeagueForm, name='formLeague'),
    path('leagueList/', views.leagueList, name='leagueList'),
    path('deleteLeague/<int:id>/', views.deleteLeague, name='deleteLeague'),
    path('editLeague/<int:id>/', views.editLeague, name='editLeague'),

    # Club
    path('formClub/', views.ClubForm, name='formClub'),
    path('clubList/', views.clubList, name='clubList'),
    path('deleteClub/<int:id>/', views.deleteClub, name='deleteClub'),
    path('editClub/<int:id>/', views.editClub, name='editClub'),

    # TopMatch
    path('formTopMatch/', views.top_match_create, name='top_match_create'),
    path('topMatchList/', views.topMatchList, name='topMatchList'),
    path('deleteTopMatch/<int:id>/', views.deleteTopMatch, name='deleteTopMatch'),
    path('editTopMatch/<int:id>/', views.editTopMatch, name='editTopMatch'),

    # NextToGo
    path('formNextToGo/', views.NextToGoForm, name='formNextToGo'),
    path('nextToGoList/', views.nextToGoList, name='nextToGoList'),
    path('deleteNextToGo/<int:id>/', views.deleteNextToGo, name='deleteNextToGo'),
    path('editNextToGo/<int:id>/', views.editNextToGo, name='editNextToGo'),

    # Trending
    path('formTrending/', views.TrendingForm, name='formTrending'),
    path('trendingList/', views.trendingList, name='trendingList'),
    path('deleteTrending/<int:id>/', views.deleteTrending, name='deleteTrending'),
    path('editTrending/<int:id>/', views.editTrending, name='editTrending'),
]