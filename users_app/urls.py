from django.urls import path ,include
from todolist_app import views
from users_app import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('registration', views.registration, name="registration"),
    path('login', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout', auth_views.LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
    #path('logout', views.debug_logout , name='logout'),
]
