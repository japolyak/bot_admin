# Generated by Django 4.1.1 on 2022-09-27 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_clientcarts_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientcarts',
            old_name='product_id',
            new_name='product',
        ),
    ]