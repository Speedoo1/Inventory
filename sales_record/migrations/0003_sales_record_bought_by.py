# Generated by Django 4.1.3 on 2023-03-03 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('sales_record', '0002_remove_sales_record_bought_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales_record',
            name='bought_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
    ]
