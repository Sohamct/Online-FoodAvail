

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0011_remove_product_due_alter_product_cur_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='due',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='cur_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='exp_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
