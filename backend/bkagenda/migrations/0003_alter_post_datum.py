# Generated by Django 3.2.25 on 2024-04-18 06:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bkagenda', '0002_rename_date_post_datum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='datum',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
