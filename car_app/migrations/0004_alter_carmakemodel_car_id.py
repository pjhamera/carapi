# Generated by Django 4.0.1 on 2022-01-14 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0003_remove_carmakemodel_id_carmakemodel_car_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmakemodel',
            name='car_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
