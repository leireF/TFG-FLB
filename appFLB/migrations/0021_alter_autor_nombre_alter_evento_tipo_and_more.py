# Generated by Django 4.0.1 on 2022-04-05 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appFLB', '0020_socio_apellido_alter_socio_nif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='nombre',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='evento',
            name='tipo',
            field=models.CharField(choices=[('Seminarios de apoyo en matemáticas y mat. financieras', 'seminarios de apoyo en matemáticas y mat. financieras'), ('Tedx', 'tedx'), ('Patrocinio Trabajos Investigación', 'patrocinio trabajos investigación'), ('London Finance Seminar', 'london finance seminar')], max_length=70),
        ),
        migrations.AlterField(
            model_name='libro',
            name='sinopsis',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='socio',
            name='apellido',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
