# Generated by Django 4.1.1 on 2022-09-26 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Location')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Property title')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('price', models.IntegerField(default=0, verbose_name='Price')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Date')),
                ('location', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='dashboard.location')),
            ],
        ),
        migrations.CreateModel(
            name='Propertyimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='property-image', verbose_name='Property Image')),
                ('type', models.CharField(choices=[('BD', 'Bad Room'), ('LR', 'Living Room'), ('BT', 'Bath Room'), ('WS', 'Wash Room'), ('DI', 'Dining Room')], max_length=50, verbose_name='Property Type')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='dashboard.property')),
            ],
        ),
    ]
