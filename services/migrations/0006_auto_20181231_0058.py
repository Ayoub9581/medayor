# Generated by Django 2.1.3 on 2018-12-31 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20181231_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
