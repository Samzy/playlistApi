# Generated by Django 2.0.6 on 2018-06-14 15:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playlist',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
