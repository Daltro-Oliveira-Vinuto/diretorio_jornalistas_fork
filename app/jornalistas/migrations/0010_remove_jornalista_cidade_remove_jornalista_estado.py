# Generated by Django 4.2.4 on 2023-10-24 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jornalistas', '0009_remove_jornalista_obras_jornalisticas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jornalista',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='jornalista',
            name='estado',
        ),
    ]
