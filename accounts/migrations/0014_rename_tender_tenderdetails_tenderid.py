# Generated by Django 4.0.5 on 2023-10-02 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_tenderdetails_tender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tenderdetails',
            old_name='tender',
            new_name='tenderId',
        ),
    ]