# Generated by Django 4.2 on 2024-04-16 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webPages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flan',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]