# Generated by Django 4.0.1 on 2022-06-29 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customer_mobileno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobileNo',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]