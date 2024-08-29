from django.shortcuts import render, redirect
from .forms import SiteCheckerForm, LoginForm
from .models import SiteChecker
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import SiteChecker


@login_required
def home_view(request):
    user = request.user
    datas = SiteChecker.objects.filter(name=user)
    # print(datas)
    if datas.exists():
        context = {"datas": datas}
    else:
        context = {"msg": "No any data is exists for text"}
    return render(request, "home_page.html", context=context)


@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login_page")
    return render(request, "logout.html")


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_page")
    else:
        form = UserCreationForm()
    return render(request, "register.html", context={"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            UserName = form.cleaned_data.get("username")
            Password = form.cleaned_data.get("password")
            user = authenticate(request, username=UserName, password=Password)
            if user is not None:
                login(request, user)
                messages.success(request, "login successfully")
                return redirect("add_site_page")
            else:
                messages.error(request, "invalid username and password!")
    form = LoginForm()
    return render(request, "login_page.html", context={"form": form})


@login_required
def add_site(request):
    if request.method == "POST":
        form = SiteCheckerForm(request.POST)
        if form.is_valid():
            name = request.user
            slack_url = form.cleaned_data.get("slack_url")
            web_url = form.cleaned_data.get("web_url")
            url_text = form.cleaned_data.get("url_text")
            text = form.cleaned_data.get("text")
            frequency = form.cleaned_data.get("frequency")
            SiteChecker.objects.create(
                name=name,
                slack_url=slack_url,
                web_url=web_url,
                url_text=url_text,
                text=text,
                frequency=frequency,
            )
            return redirect("home_page")
    else:
        form = SiteCheckerForm()
    return render(request, "add_sites.html", context={"form": form})
