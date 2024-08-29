from django import forms
from .models import SiteChecker

# from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=500, label="username")
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "password"})
    )


# class SiteCheckerForm(forms.Form):
#     slack_url = forms.URLField(max_length=2000, label="slack_url")
#     web_url = forms.URLField(max_length=2000, label="web_url")
#     url_text = forms.CharField(max_length=2000, default="SIte Link")
#     text = forms.CharField(max_length=200)
#     frequency = forms.DurationField()


class SiteCheckerForm(forms.ModelForm):
    class Meta:
        model = SiteChecker
        fields = ["slack_url", "web_url", "url_text", "text"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "slack_url": forms.URLInput(attrs={"class": "form-control"}),
            "web_url": forms.URLInput(attrs={"class": "form-control"}),
            "url_text": forms.TextInput(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"}),
        }
