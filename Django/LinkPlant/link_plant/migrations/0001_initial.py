# Generated by Django 5.0.4 on 2024-04-17 05:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, verbose_name='slug')),
                ('bg_color', models.CharField(choices=[('brown', 'Brown'), ('pink', 'Pink'), ('orange', 'Orange'), ('red', 'Red'), ('yellow', 'Yellow'), ('green', 'Green'), ('blue', 'Blue')], max_length=20, verbose_name='color')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='link_plant.profile')),
            ],
        ),
    ]