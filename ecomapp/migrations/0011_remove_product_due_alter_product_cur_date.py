

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0010_product_cur_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='due',
        ),
        migrations.AlterField(
            model_name='product',
            name='cur_date',
            field=models.DateField(default=django.utils.datetime_safe.date.today),
        ),
    ]
