# Generated by Django 2.2.10 on 2020-09-12 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_auto_20200912_1811'),
        ('purchase', '0002_auto_20200912_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product')),
                ('purchase_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='purchase.Purchase')),
            ],
            options={
                'verbose_name': 'purchaseproduct',
                'verbose_name_plural': 'purchaseproducts',
            },
        ),
    ]