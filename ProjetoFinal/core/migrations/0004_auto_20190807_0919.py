# Generated by Django 2.2.1 on 2019-08-07 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_movimentorotativo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movimentorotativo',
            old_name='velor_hora',
            new_name='valor_hora',
        ),
    ]
