# Generated by Django 2.1.5 on 2019-02-04 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20190201_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='firstapp/photos', verbose_name='Фото'),
        ),
    ]