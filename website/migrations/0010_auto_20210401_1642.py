# Generated by Django 3.1.6 on 2021-04-01 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20210331_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='date_presented',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='archive',
            name='decision',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='archive',
            name='notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
