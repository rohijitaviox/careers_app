# Generated by Django 4.1.4 on 2022-12-19 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0013_alter_job_jobtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduleinterview',
            name='candidate',
        ),
        migrations.RemoveField(
            model_name='scheduleinterview',
            name='job',
        ),
        migrations.DeleteModel(
            name='Candidate',
        ),
        migrations.DeleteModel(
            name='ScheduleInterview',
        ),
    ]
