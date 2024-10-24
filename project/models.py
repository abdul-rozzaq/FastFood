from django.db import models


class FoodType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Food Type")

    class Meta:
        verbose_name = "Food Type"
        verbose_name_plural = "Food Types"

    def __str__(self):
        return self.name


class Food(models.Model):
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE, verbose_name="Turi")
    name = models.CharField(max_length=100, verbose_name="Nomi")
    ingredients = models.TextField(verbose_name="Tarkibi")
    price = models.IntegerField(verbose_name="Narxi")
    views_count = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")
    image = models.ImageField(upload_to="foods/", verbose_name="Rasmi", null=True, blank=True)

    class Meta:
        verbose_name = "Food"
        verbose_name_plural = "Foods"

    def __str__(self):
        return self.name
