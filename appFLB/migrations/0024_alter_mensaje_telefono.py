# Generated by Django 4.0 on 2022-04-17 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appFLB', '0023_alter_mensaje_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='telefono',
            field=models.PositiveIntegerField(),
        ),
    ]