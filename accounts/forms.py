from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate, login , logout, get_user_model
import unicodedata
from django.utils.text import capfirst
from django.utils.translation import gettext, gettext_lazy as _

User = get_user_model()

class UsernameField(forms.CharField):
    def to_python(self, value):
        return unicodedata.normalize('NFKC', super().to_python(value))

class LoginForm(forms.Form):
    phone = UsernameField(max_length=12,
                            widget=forms.TextInput(attrs={
                                'type': 'tel',
                                'placeholder': 'Мобильный номер',
                                'autofocus': True,
                                }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'autofocus': True})

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Придумайте пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль еще раз'}))

    class Meta:
        model = User
        fields = ['phone', 'first_name']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({
            'placeholder': 'Мобильный номер'
        })
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'Имя пользователья'
        })

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        qs = User.objects.filter(phone = 'phone')
        if qs.exists():
            raise forms.ValidationError("Вы уже зарегистрированы!")
        return phone

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user

class UserAdminCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['phone', 'first_name']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совподают")
        return password2

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = [ 'phone', 'first_name','password', 'active', 'admin']

    def clean_password(self):
        return self.initial["password"]