# Generated by Django 5.0.6 on 2024-06-27 13:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frio', '0002_camaras_umbrales'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='camaras',
            options={'verbose_name': 'Cámara', 'verbose_name_plural': 'Cámaras'},
        ),
        migrations.AlterModelOptions(
            name='umbrales',
            options={'verbose_name': 'Umbral', 'verbose_name_plural': 'Umbrales'},
        ),
        migrations.AlterField(
            model_name='umbrales',
            name='ix',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Camaras_ix', to='frio.camaras', verbose_name='Canal'),
        ),
    ]
