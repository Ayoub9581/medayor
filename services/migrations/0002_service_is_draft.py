# Generated by Django 2.1.3 on 2018-12-30 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='is_draft',
            field=models.BooleanField(default=False),
        ),
    ]
