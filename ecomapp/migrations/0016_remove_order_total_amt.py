# Generated by Django 4.1.7 on 2023-04-10 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0015_order_total_amt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_amt',
        ),
    ]