from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', views, name=),
    path('login/', auth_views.LoginView.as_view(
        template_name='usuario/form.html'
    ), name='loginView'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='usuario/form.html'
    ), name='logoutView'),
]