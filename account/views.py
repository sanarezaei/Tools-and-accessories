from django.shortcuts import render
from django import views
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import LoginForm

class LoginView(views):
    template_name = 'login.html'
    
    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
        
            user = authenticate(request, username=phone_number, password=password)
            
            if user is not None:
                login(request, user)
                
                messages.success(request, "شما با موفقیت وارد شدید.")
                return redirect('home')
            else:
                messages.error(request,\
                    "شماره تلفن یا رمز عبور شما نامعتبر است.")
        else:
            messages.error(request, "لطفا فرم ورود را به درستی تکمیل کنید.")
            
        return render(request, self.template_name, {'form': form})
            
        