# Generated by Django 4.2 on 2024-04-23 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webPages', '0005_flan_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flan',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
