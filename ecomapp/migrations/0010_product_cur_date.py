

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0009_product_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cur_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
