# Generated by Django 4.2.7 on 2023-11-23 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vendor_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('contact_details', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('vendor_code', models.CharField(blank=True, max_length=500, null=True, unique=True)),
                ('on_time_delivery_rate', models.FloatField(blank=True, null=True)),
                ('quality_rating_avg', models.FloatField(blank=True, null=True)),
                ('average_response_time', models.FloatField(blank=True, null=True)),
                ('fulfillment_rate', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='po_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.CharField(blank=True, max_length=500, null=True, unique=True)),
                ('order_date', models.DateTimeField(blank=True, null=True)),
                ('delivery_date', models.DateTimeField(blank=True, null=True)),
                ('items', models.JSONField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=500, null=True)),
                ('quality_rating', models.FloatField(blank=True, null=True)),
                ('issue_date', models.DateTimeField(blank=True, null=True)),
                ('acknowledgment_date', models.DateTimeField(blank=True, null=True)),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='po.vendor_details')),
            ],
        ),
        migrations.CreateModel(
            name='performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('on_time_delivery_rate', models.FloatField(blank=True, null=True)),
                ('quality_rating_avg', models.FloatField(blank=True, null=True)),
                ('average_response_time', models.FloatField(blank=True, null=True)),
                ('fulfillment_rate', models.FloatField(blank=True, null=True)),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='po.vendor_details')),
            ],
        ),
    ]
