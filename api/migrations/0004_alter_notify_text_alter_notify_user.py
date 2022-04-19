# Generated by Django 4.0.3 on 2022-04-19 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_notify_id_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notify',
            name='Text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='notify',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notify', to='api.user'),
        ),
    ]
