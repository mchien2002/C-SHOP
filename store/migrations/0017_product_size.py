# Generated by Django 4.0.3 on 2022-04-24 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_remove_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='store.size'),
        ),
    ]
