# project/users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)
    nickname = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'nickname')
        labels = {
            'email': '이메일',
            'password1': '비밀번호',
            'password2': '비밀번호 확인',
            'nickname': '닉네임',
        }
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['email'].label = '이메일'
            self.fields['password1'].label = '비밀번호'
            self.fields['password2'].label = '비밀번호 확인'
            self.fields['nickname'].label = '닉네임'

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
