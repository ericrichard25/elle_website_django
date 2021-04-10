# Generated by Django 3.1.6 on 2021-03-31 20:16

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NAV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nav', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quintile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quintile', models.CharField(blank=True, default='', max_length=255)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Top_Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=255)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=3)),
                ('publication_date', models.DateField()),
                ('publication_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('peak_date', models.DateField(null=True)),
                ('peak_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('peak_return', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('days', models.IntegerField(null=True)),
                ('years', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('annualized_return', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('password', models.CharField(max_length=255)),
                ('permission', models.CharField(max_length=255)),
                ('active', models.BooleanField(blank=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=255)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('first_pt', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('first_upside', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('consensus_pt', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('consensus_upside', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('analysis_date', models.DateField(blank=True)),
                ('analysis_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('summary', models.TextField(blank=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('target_position', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=15)),
                ('last_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('buy_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('quintile', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='contains', to='website.quintile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True)),
                ('decision', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('analyst', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='commented', to='website.user')),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='website.stock')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_assigned', models.DateField(blank=True)),
                ('priority', models.IntegerField(blank=True)),
                ('date_presented', models.DateField(blank=True)),
                ('decision', models.CharField(blank=True, max_length=255)),
                ('notes', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('analyst', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assignments', to='website.user')),
                ('previous_analyst', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='previous_assignments', to='website.user')),
                ('symbol', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='assigned', to='website.stock')),
            ],
        ),
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_assigned', models.DateField(blank=True)),
                ('priority', models.IntegerField(blank=True)),
                ('date_presented', models.DateField(blank=True)),
                ('decision', models.CharField(blank=True, max_length=255)),
                ('notes', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('analyst', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='archives', to='website.user')),
                ('previous_analyst', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='previously_assigned', to='website.user')),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='archives', to='website.stock')),
            ],
        ),
    ]
