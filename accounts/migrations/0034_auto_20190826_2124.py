# Generated by Django 2.2.4 on 2019-08-26 18:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_auto_20190821_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentpresence',
            name='Attendance_Date',
            field=models.DateField(default=datetime.datetime(2019, 8, 26, 18, 24, 8, 566164, tzinfo=utc)),
        ),
    ]
