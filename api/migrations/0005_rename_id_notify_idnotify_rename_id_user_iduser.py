# Generated by Django 4.0.3 on 2022-04-19 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_notify_text_alter_notify_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notify',
            old_name='id',
            new_name='idNotify',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='id',
            new_name='idUser',
        ),
    ]