# Generated by Django 4.0.5 on 2023-10-11 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_rename_quatation_status_quotation_quotation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='tender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotations', to='accounts.tender'),
        ),
    ]
