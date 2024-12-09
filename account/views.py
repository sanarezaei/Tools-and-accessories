from django.shortcuts import render
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import LoginForm

class HomeView(View):
    def get(self, request):
        user = self.request.user
        phone_number = None
        
        if user.is_authenticated:
            phone_number = user.phone_number
        return render(request, 'account/home.html', 
                    context={'phone_number': phone_number})

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'account/login.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        phone_number = form.cleaned_data.get('phone_number')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, phone_number=phone_number, password=password)
        
        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'با موفقیت وارد شدید.')
            return super().form_valid(form)
        else:
            messages.error(self.request, 'نام کاربری یا رمز عبور اشتباه است.')
            return super().form_invalid(form)
        