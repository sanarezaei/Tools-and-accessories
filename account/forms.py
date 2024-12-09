from django import forms 

class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'شماره تلفن',
            'class': 'form-control'}), 
        label="Phone Number")
    
    password = forms.CharField(\
        widget=forms.PasswordInput(
            attrs={'placeholder': 'رمز عبور', 'class': 'form-control'}), 
        label="Password")
