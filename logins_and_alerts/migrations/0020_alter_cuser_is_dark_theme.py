# Generated by Django 4.2.14 on 2024-08-29 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logins_and_alerts', '0019_alter_cuser_is_dark_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuser',
            name='is_dark_theme',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='false', max_length=5),
        ),
    ]
