
from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0006_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='exp_date',
            field=models.DateField(default=django.utils.datetime_safe.date.today),
        ),
    ]
