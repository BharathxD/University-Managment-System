# Generated by Django 4.1.2 on 2022-12-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=70)),
                ('password', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=70)),
                ('password', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=70)),
                ('password', models.CharField(max_length=70)),
            ],
        ),
    ]