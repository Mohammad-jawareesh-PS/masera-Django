# Generated by Django 4.0.2 on 2022-02-20 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_school', '0002_user_delete_signup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=300, unique=True),
        ),
    ]