# Generated by Django 4.2.7 on 2023-11-06 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medapi', '0002_remove_medicine_remaining_stock_medicine_expiry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='company',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
