# Generated by Django 4.0.3 on 2022-04-19 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_notify_id_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notify',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
