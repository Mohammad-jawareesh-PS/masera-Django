# Generated by Django 4.0.2 on 2022-02-21 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_school', '0003_alter_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='category',
            new_name='calss',
        ),
    ]