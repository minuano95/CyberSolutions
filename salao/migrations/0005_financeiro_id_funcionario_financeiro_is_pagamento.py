# Generated by Django 5.0.1 on 2024-03-20 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salao', '0004_remove_agendamento_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='financeiro',
            name='id_funcionario',
            field=models.BooleanField(blank=True, default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='financeiro',
            name='is_pagamento',
            field=models.BooleanField(default=False),
        ),
    ]
