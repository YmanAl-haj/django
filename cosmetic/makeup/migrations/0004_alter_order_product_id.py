# Generated by Django 4.0.1 on 2022-01-31 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('makeup', '0003_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makeup.products'),
        ),
    ]