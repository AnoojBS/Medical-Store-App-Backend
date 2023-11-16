# Generated by Django 4.2.7 on 2023-11-06 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medapi', '0003_medicine_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='quantity',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
