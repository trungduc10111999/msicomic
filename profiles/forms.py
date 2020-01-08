from captcha.fields import ReCaptchaField
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()


class RegisterForm(UserCreationForm):
    capcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email')
        field_classes = {'username': UsernameField}
        widgets = {
            'email': forms.EmailInput(attrs={'required': True})
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('full_name', 'address', 'year_birth', 'about')
