# Generated by Django 3.1.6 on 2021-03-31 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20210331_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='analyst',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='archives', to='website.user'),
        ),
        migrations.AlterField(
            model_name='archive',
            name='previous_analyst',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='previously_assigned', to='website.user'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='previous_analyst',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='previous_assignments', to='website.user'),
        ),
    ]
