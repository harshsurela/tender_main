# Generated by Django 4.0.1 on 2022-06-29 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_customer_mobileno'),
    ]

    operations = [
        migrations.AddField(
            model_name='tender',
            name='fullFilled',
            field=models.BooleanField(default=False),
        ),
    ]
