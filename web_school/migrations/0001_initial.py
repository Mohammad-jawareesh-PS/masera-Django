# Generated by Django 4.0.2 on 2022-02-16 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=300, null=True)),
                ('Subject', models.CharField(blank=True, max_length=150, null=True)),
                ('message', models.TextField(blank=True, max_length=4000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_class', models.CharField(max_length=250)),
                ('category', models.CharField(choices=[('basic stage', 'basic stage'), ('eleventh grade', 'eleventh grade'), ('Twelfth grade', 'Twelfth grade')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_content', models.CharField(max_length=250)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contents', to='web_school.class')),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=300)),
                ('username', models.CharField(max_length=250, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('confirm_password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_unit', models.CharField(max_length=250)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='units', to='web_school.content')),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_summary', models.CharField(max_length=250)),
                ('img_duty', models.ImageField(blank=True, null=True, upload_to='duty_Summary')),
                ('file', models.FileField(blank=True, null=True, upload_to='Summary_file')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='summarys', to='web_school.unit')),
            ],
        ),
        migrations.CreateModel(
            name='Explain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_explain', models.CharField(max_length=250)),
                ('img_duty', models.ImageField(blank=True, null=True, upload_to='Explain_img')),
                ('file', models.FileField(blank=True, null=True, upload_to='Explain_file')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='explains', to='web_school.unit')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_exam', models.CharField(max_length=250)),
                ('img_duty', models.ImageField(blank=True, null=True, upload_to='Exam_img')),
                ('file', models.FileField(blank=True, null=True, upload_to='Exam_file')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exams', to='web_school.unit')),
            ],
        ),
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_duty', models.CharField(max_length=250)),
                ('img_duty', models.ImageField(blank=True, null=True, upload_to='duty_img')),
                ('file', models.FileField(blank=True, null=True, upload_to='duty_file')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dutys', to='web_school.unit')),
            ],
        ),
    ]
