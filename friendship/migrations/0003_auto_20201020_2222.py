# Generated by Django 3.1 on 2020-10-20 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendship', '0002_auto_20201020_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
