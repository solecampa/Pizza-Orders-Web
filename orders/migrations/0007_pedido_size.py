# Generated by Django 3.0.6 on 2020-06-02 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200602_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='size',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
