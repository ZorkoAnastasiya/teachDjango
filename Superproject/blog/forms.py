import re
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Post


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "hidden", "rubric"]
        widgets = {
            "title": forms.TextInput(attrs = {"class": "form-control"}),
            "content": forms.Textarea(attrs = {"class": "form-control", "rows": 7}),
            "rubric": forms.Select(attrs = {"class": "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if re.match(r"\d", title):
            raise ValidationError("There should be no numbers at the beginning")
        return title


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label = "Username",
        widget = forms.TextInput(attrs = {"class": "form-control"})
    )
    email = forms.EmailField(
        label = "Email address",
        widget = forms.EmailInput(attrs = {"class": "form-control"})
    )
    password1 = forms.CharField(
        label = "Password",
        widget =forms.PasswordInput(attrs = {"class": "form-control"})
    )
    password2 = forms.CharField(
        label = "Password confirmation",
        widget =forms.PasswordInput(attrs = {"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label = "Username",
        widget = forms.TextInput(attrs = {"class": "form-control"})
    )
    password = forms.CharField(
        label = "Password",
        widget = forms.PasswordInput(attrs = {"class": "form-control"})
    )
