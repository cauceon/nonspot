# Generated by Django 2.0.6 on 2020-04-15 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluations', '0004_auto_20200415_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluation',
            name='comments',
        ),
    ]