# Generated by Django 3.0.7 on 2020-06-04 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_pedido_topping'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
