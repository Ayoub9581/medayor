# Generated by Django 2.1.3 on 2019-01-02 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20190102_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='host_contact',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='server_name_contact',
        ),
    ]
