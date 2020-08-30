from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .forms import AddPageForm, CreateUserForm
from .models import *
from .decorators import *


@unauthenticated
def sign_up(request):
    form = CreateUserForm(request.POST or None)

    if form.is_valid():
        user = form.save()

        username = form.cleaned_data.get('username')
        messages.success(request, 'Hi '+username+' welcome to DearDiary')
        return redirect('home')
    context = {
        "form": form
    }

    return render(request, "diary/sign_up.html", context)


def logoutUser(request):
    logout(request)
    return redirect("login")


@unauthenticated
def loginPage(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Username or password is incorrect")

    context = {}
    return render(request, "diary/login.html", context)


@login_required(login_url='login')
def home(request):

    pages = DiaryPage.objects.all().order_by('-date_page')

    context = {"pages": pages}

    return render(request, "diary/home.html", context)


@login_required(login_url='login')
def add_page(request):
    form = AddPageForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/")

    context = {
        "form": form
    }
    return render(request, "diary/add_page.html", context)


@login_required(login_url='login')
def update_page(request, pk):
    page = DiaryPage.objects.get(id=pk)
    form = AddPageForm(request.POST or None, instance=page)

    if form.is_valid():
        form.save()
        return redirect("/")

    context = {
        "form": form
    }
    return render(request, "diary/add_page.html", context)


@login_required(login_url='login')
def delete_page(request, pk):
    page = DiaryPage.objects.get(id=pk)
    if request.method == "POST":
        page.delete()
        return redirect("/")
    return render(request, "diary/delete.html")


@login_required(login_url='login')
def page(request, pk):
    page = DiaryPage.objects.get(id=pk)

    context = {"page": page}

    return render(request, "diary/page.html", context)
