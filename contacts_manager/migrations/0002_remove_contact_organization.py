# Generated by Django 4.2.7 on 2023-11-12 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='organization',
        ),
    ]