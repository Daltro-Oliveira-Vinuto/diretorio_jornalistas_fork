# Generated by Django 4.1.4 on 2023-10-27 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('associacoes', '0003_remove_associacao_ddd_telefone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associacao',
            name='telefone',
            field=models.CharField(max_length=10),
        ),
    ]
