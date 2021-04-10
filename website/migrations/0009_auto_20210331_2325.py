# Generated by Django 3.1.6 on 2021-03-31 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20210331_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='archive',
            name='archiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='archived', to='website.user'),
        ),
        migrations.AlterField(
            model_name='top_idea',
            name='symbol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='top_ideas', to='website.stock'),
        ),
    ]
