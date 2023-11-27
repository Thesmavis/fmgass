# Generated by Django 4.2.7 on 2023-11-23 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('po', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='po_details',
            name='status',
            field=models.IntegerField(choices=[(1, 'Generated'), (2, 'Accepted'), (3, 'Pending'), (4, 'Cancelled'), (5, 'Completed')], default=1),
        ),
    ]
