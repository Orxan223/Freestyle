# Generated by Django 3.2.6 on 2021-09-08 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_index_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='index',
            name='email',
        ),
    ]
