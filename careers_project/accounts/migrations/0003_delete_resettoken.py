# Generated by Django 4.1.4 on 2022-12-15 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_resettoken_token_alter_resettoken_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ResetToken',
        ),
    ]
