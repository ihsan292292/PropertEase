# Generated by Django 4.2 on 2023-12-28 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_property_tenant_unit_tenantunitassignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='photo',
            field=models.FileField(default=1, upload_to='tenant_photo'),
            preserve_default=False,
        ),
    ]
