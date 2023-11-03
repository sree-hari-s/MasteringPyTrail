from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('register',views.register,name='register'),
    path('logoutuser',views.logoutuser,name='logoutuser'),
    path('home',views.home,name='home'),
    path('addlist',views.addlist,name='addlist'),
    path('delete/<str:pk>',views.delete,name='delete')
]