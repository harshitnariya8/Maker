# Generated by Django 4.0.1 on 2022-08-23 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0002_alter_category_restaurant_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='restaurant_id',
            field=models.IntegerField(),
        ),
    ]
