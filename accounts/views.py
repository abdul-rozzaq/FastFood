from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.core.handlers.wsgi import WSGIRequest

from .forms import UserRegisterForm, UserLoginForm


def user_register(request: WSGIRequest):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect("home")
    else:
        form = UserRegisterForm()

    context = {"form": form}

    return render(request, "accounts/register.html", context)


def user_login(request: WSGIRequest):
    next = request.GET.get("next")

    if request.method == "POST":
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            login(request=request, user=form.get_user())

            return redirect(next or "home")

    else:
        form = UserLoginForm()

    context = {"form": form}

    return render(request, "accounts/login.html", context)


def user_logout(request: WSGIRequest):

    logout(request)

    return redirect("accounts:login")
