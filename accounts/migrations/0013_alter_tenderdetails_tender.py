# Generated by Django 4.0.5 on 2023-10-02 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_remove_customer_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenderdetails',
            name='tender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tender', to='accounts.tender'),
        ),
    ]