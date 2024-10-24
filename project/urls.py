from django.urls import path
from .views import home_page, detail_page, delete_food


urlpatterns = [
    path("", home_page, name="home"),
    path("food/<int:pk>/", detail_page, name="food_detail"),
    path("food/<int:pk>/delete/", delete_food, name="food_delete"),
]
