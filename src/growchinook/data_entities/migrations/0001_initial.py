# Generated by Django 3.2.9 on 2021-12-03 21:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depth', models.FloatField(help_text='Depth in meters')),
                ('year', models.IntegerField()),
                ('month', models.IntegerField(help_text='Month (1-12)', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('temperature', models.FloatField(help_text='Temperature in degrees C')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_entities.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PreyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depth', models.FloatField(help_text='Depth in meters')),
                ('year', models.IntegerField()),
                ('month', models.IntegerField(help_text='Month (1-12)', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('species', models.CharField(choices=[('DAPNHIA', 'Daphnia')], max_length=64)),
                ('abundance', models.IntegerField()),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_entities.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bathymetry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elevation', models.FloatField()),
                ('area2d', models.FloatField()),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_entities.site')),
            ],
        ),
        migrations.AddIndex(
            model_name='temperature',
            index=models.Index(fields=['site', 'year', 'month'], name='data_entiti_site_id_7d1534_idx'),
        ),
        migrations.AddIndex(
            model_name='preydata',
            index=models.Index(fields=['site', 'year', 'month'], name='data_entiti_site_id_2a07aa_idx'),
        ),
    ]