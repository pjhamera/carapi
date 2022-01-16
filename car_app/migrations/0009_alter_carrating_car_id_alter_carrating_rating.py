# Generated by Django 4.0.1 on 2022-01-15 11:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0008_remove_car_avg_rating_remove_car_rates_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrating',
            name='car_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='car_app.car'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carrating',
            name='rating',
            field=models.PositiveBigIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
    ]
