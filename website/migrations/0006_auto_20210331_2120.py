# Generated by Django 3.1.6 on 2021-03-31 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20210331_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='date_assigned',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='date_presented',
            field=models.DateField(blank=True, null=True),
        ),
    ]
