
from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0012_product_due_alter_product_cur_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='exp_date',
            field=models.DateField(default=django.utils.datetime_safe.date.today),
        ),
    ]
