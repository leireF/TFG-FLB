# Generated by Django 4.0.1 on 2022-02-03 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appFLB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulo',
            name='temas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appFLB.tema'),
        ),
    ]