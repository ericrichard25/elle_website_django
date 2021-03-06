# Generated by Django 3.1.6 on 2021-04-05 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20210401_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='symbol',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='assigned', to='website.stock'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='symbol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='website.stock'),
        ),
    ]
