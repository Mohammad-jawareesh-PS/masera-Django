# Generated by Django 4.0.2 on 2022-03-01 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_school', '0011_content_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duty',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dutys', to='web_school.content'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exams', to='web_school.content'),
        ),
        migrations.AlterField(
            model_name='explain',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='explains', to='web_school.content'),
        ),
        migrations.AlterField(
            model_name='summary',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='summarys', to='web_school.content'),
        ),
        migrations.DeleteModel(
            name='Unit',
        ),
    ]
