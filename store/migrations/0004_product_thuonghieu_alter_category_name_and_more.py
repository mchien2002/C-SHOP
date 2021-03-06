# Generated by Django 4.0.3 on 2022-03-24 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thuonghieu',
            field=models.CharField(default='Unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='Unknown', on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
    ]
