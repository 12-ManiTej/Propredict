from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from .views import sign_up

urlpatterns = [
    #  path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('signup/', sign_up, name='signup'),
    # path("register",views.register,name="register"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('',views.index,name="index"),
    path('home',views.home,name="home"),
    path('home/home_details/<int:pk>/',views.home_details,name="home_details"),
    path('predict',views.predict,name="predict"),
    path('result',views.result,name="result"),
    path('about',views.about,name="about"),
    path("contact",views.contact,name="contact"),
] 