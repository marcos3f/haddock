# Generated by Django 3.1 on 2019-12-08 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('haddock', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incidente',
            name='pub_date',
        ),
    ]