from django .urls import path
from . import views

urlpatterns = [
    path('index1/', views.index1, name='index1'),
    path('user_login/', views.user_login, name='user_login'),
    path('register_form/', views.registration, name='register'),
]
