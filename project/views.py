from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from django.core.handlers.wsgi import WSGIRequest

from project.models import Food
from .forms import FoodForm


def home_page(request: WSGIRequest):

    user = request.user

    if request.method == "POST" and user.has_perm("project.add_food"):
        form = FoodForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()

    else:
        form = FoodForm()

    foods = Food.objects.all()

    context = {"foods": foods, "form": form}

    return render(request, "home.html", context)


@login_required(login_url="accounts:login")
def detail_page(request, pk: int):
    food = get_object_or_404(Food, pk=pk)
    foods = Food.objects.exclude(pk=food.pk)

    if request.method == "POST":
        form = FoodForm(instance=food, data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()

    else:
        form = FoodForm(instance=food)

    food.views_count += 1
    food.save()

    context = {"food": food, "foods": foods, "form": form}

    return render(request, "detail.html", context)


@login_required(login_url="login")
@permission_required(["project.delete_food"], login_url="login")
def delete_food(request, pk: int):

    food = get_object_or_404(Food, pk=pk)

    food.delete()

    return redirect("home")
