

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0008_remove_product_return_policy_remove_product_warranty_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='due',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
