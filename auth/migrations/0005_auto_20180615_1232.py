# Generated by Django 2.0.6 on 2018-06-15 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_auth', '0004_auto_20180615_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotifyuser',
            name='scope',
            field=models.CharField(max_length=255),
        ),
    ]