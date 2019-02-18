# Generated by Django 2.1.5 on 2019-01-21 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_pizza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='pizzashop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.PizzaShop', verbose_name='Магазин'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='short_description',
            field=models.CharField(max_length=10, verbose_name='Краткое описание'),
        ),
    ]
