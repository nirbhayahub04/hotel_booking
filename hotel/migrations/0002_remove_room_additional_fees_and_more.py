# Generated by Django 5.0 on 2025-03-13 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='additional_fees',
        ),
        migrations.RemoveField(
            model_name='room',
            name='seasonal_pricing',
        ),
        migrations.AddConstraint(
            model_name='hotelimage',
            constraint=models.UniqueConstraint(condition=models.Q(('is_primary', True)), fields=('hotel',), name='unique_primary_image_per_hotel'),
        ),
    ]
