# Generated by Django 4.2.7 on 2023-11-25 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('po', '0002_alter_po_details_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='po_details',
            old_name='delivery_date',
            new_name='ex_delivery_date',
        ),
        migrations.AddField(
            model_name='po_details',
            name='act_delivery_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
