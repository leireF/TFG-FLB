# Generated by Django 4.0.1 on 2022-04-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appFLB', '0021_alter_autor_nombre_alter_evento_tipo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='sinopsis',
            field=models.TextField(blank=True, default=''),
        ),
    ]
