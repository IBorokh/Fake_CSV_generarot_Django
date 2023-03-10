from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


app_name = 'login'

urlpatterns = [
    path('', views.SignInView.as_view(), name='signin'),
    path('sign_up/', views.SignUpView.as_view(), name='signup'),
    path('logout', LogoutView.as_view(), name='signout')
]
