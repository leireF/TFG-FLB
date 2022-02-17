# Generated by Django 4.0.1 on 2022-02-14 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appFLB', '0016_alter_miembro_fechafin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edicionbeca',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='edicionpremio',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='libro',
            name='fecha_publicacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='miembro',
            name='fechaComienzo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='socio',
            name='fecha_alta',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='socio',
            name='fecha_baja',
            field=models.DateField(blank=True, null=True),
        ),
    ]