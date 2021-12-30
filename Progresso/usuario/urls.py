from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate

urlpatterns = [
    #path('', views, name=),
    path('login/', auth_views.LoginView.as_view(
        template_name='usuario/login.html'
    ), name='loginView'),
    path('logout/', auth_views.LogoutView.as_view(), name='logoutView'),
    path('cadUser/', UsuarioCreate.as_view(), name='cadUser')
]