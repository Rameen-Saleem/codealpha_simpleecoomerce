# Generated by Django 5.2.3 on 2025-07-03 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_order_order_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
