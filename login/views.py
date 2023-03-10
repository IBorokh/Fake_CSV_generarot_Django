from .forms import SignUpForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class SignInView(LoginView):
    template_name = 'login/signin.html'
    next_page = reverse_lazy('datasets:dashboard')


class SignUpView(CreateView):
    template_name = 'login/signup.html'
    success_url = reverse_lazy('login:signin')
    form_class = SignUpForm
