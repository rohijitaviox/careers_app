# Generated by Django 4.1.4 on 2022-12-19 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0014_remove_scheduleinterview_candidate_and_more'),
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
                ('position', models.CharField(max_length=100, null=True)),
                ('profile_pic', models.ImageField(null=True, upload_to='media/')),
                ('higher_education', models.CharField(max_length=200)),
                ('contact_no', models.IntegerField(null=True)),
                ('experience', models.CharField(max_length=100, null=True)),
                ('black_list', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleInterview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_ctc', models.CharField(max_length=100)),
                ('expected_ctc', models.CharField(max_length=100)),
                ('created_by', models.CharField(max_length=200)),
                ('updated_by', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('interview_date', models.DateField(null=True)),
                ('expiry_time', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('SELECTED', 'SELECTED'), ('REJECTED', 'REJECTED'), ('BLACKLISTED', 'BLACKLISTED'), ('UNDERPROCESS', 'UNDERPROCESS')], default='UNDERPROCESS', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models_app.candidate')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models_app.job')),
            ],
        ),
        migrations.CreateModel(
            name='PostLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models_app.job')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models_app.platform')),
            ],
        ),
    ]
