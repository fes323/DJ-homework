# Generated by Django 4.1.4 on 2022-12-17 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_scope_is_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='основной'),
        ),
    ]
