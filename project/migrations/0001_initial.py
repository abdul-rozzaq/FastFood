# Generated by Django 5.1.2 on 2024-10-23 19:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Food Type')),
            ],
            options={
                'verbose_name': 'Food Type',
                'verbose_name_plural': 'Food Types',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Food Name')),
                ('ingredients', models.TextField(verbose_name='Ingredients')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price')),
                ('views_count', models.IntegerField(default=0, verbose_name='Views Count')),
                ('image', models.ImageField(blank=True, null=True, upload_to='foods/', verbose_name='Food Image')),
                ('food_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.foodtype', verbose_name='Food Type')),
            ],
            options={
                'verbose_name': 'Food',
                'verbose_name_plural': 'Foods',
            },
        ),
    ]