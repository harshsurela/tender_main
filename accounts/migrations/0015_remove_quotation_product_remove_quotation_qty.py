# Generated by Django 4.0.5 on 2023-10-02 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_rename_tender_tenderdetails_tenderid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotation',
            name='product',
        ),
        migrations.RemoveField(
            model_name='quotation',
            name='qty',
        ),
    ]