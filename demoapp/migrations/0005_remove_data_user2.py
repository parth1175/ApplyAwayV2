# Generated by Django 4.0.5 on 2022-07-25 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0004_data_user2_alter_data_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='user2',
        ),
    ]