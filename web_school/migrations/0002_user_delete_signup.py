# Generated by Django 4.0.2 on 2022-02-18 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=300)),
                ('username', models.CharField(max_length=250, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Signup',
        ),
    ]
