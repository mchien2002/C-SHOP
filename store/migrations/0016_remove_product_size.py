# Generated by Django 4.0.3 on 2022-04-24 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]
