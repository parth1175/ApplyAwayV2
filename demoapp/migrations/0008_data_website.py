# Generated by Django 4.0.5 on 2022-07-24 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0007_alter_data_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='Website',
            field=models.CharField(default='LinkedIn', max_length=100),
        ),
    ]
