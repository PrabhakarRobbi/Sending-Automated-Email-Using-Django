# Generated by Django 3.0 on 2023-03-02 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0005_auto_20230220_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formdata',
            name='course',
        ),
    ]
