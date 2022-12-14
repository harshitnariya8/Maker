# Generated by Django 2.0.8 on 2022-08-15 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_price', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='media/PImage/')),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurant.Category')),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=50)),
                ('restaurant_Address', models.CharField(max_length=50)),
                ('restaurant_Contact', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=250)),
                ('logo', models.ImageField(upload_to='media/RLogo/')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=True)),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurant.RestaurantAccount')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='restaurant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurant.RestaurantAccount'),
        ),
        migrations.AddField(
            model_name='category',
            name='restaurant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurant.RestaurantAccount'),
        ),
    ]
