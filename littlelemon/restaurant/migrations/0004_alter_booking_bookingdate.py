# Generated by Django 4.1.7 on 2023-03-07 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_booking_bookingdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='BookingDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 7, 9, 48, 48, 530436)),
        ),
    ]
