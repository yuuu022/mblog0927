# Generated by Django 4.2.4 on 2023-11-29 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_maker_pmodel_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pmodel',
            name='maker',
        ),
        migrations.DeleteModel(
            name='Maker',
        ),
        migrations.DeleteModel(
            name='PModel',
        ),
    ]
