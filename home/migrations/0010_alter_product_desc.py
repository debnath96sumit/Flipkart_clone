# Generated by Django 4.0.3 on 2022-04-15 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_product_image_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
