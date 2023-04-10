
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0007_product_exp_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='return_policy',
        ),
        migrations.RemoveField(
            model_name='product',
            name='warranty',
        ),
        migrations.AddField(
            model_name='product',
            name='notice',
            field=models.CharField(default='We aim to show you accurate product information. Manufacturers, suppliers and others provide what you see here, and we have not verified it.', max_length=300),
        ),
    ]
