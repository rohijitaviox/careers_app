# Generated by Django 4.1.4 on 2022-12-16 06:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('models_app', '0004_delete_candidate_delete_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255)),
                ('profile', models.CharField(max_length=100)),
                ('higher_education', models.CharField(max_length=200)),
                ('contact_no', models.IntegerField(null=True)),
                ('experience', models.CharField(max_length=100, null=True)),
                ('black_list', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('jobtitle', models.CharField(max_length=255)),
                ('job_description', models.TextField(blank=True)),
                ('min_experience', models.CharField(max_length=255)),
                ('max_experience', models.CharField(max_length=255)),
                ('salary_min_lpa', models.CharField(max_length=255)),
                ('salary_max_lpa', models.CharField(max_length=255)),
                ('total_position', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
