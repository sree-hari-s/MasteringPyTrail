# Generated by Django 4.1 on 2023-04-22 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_fee_fee_type_alter_fee_payment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='exam_type',
            field=models.TextField(blank=True, null=True),
        ),
    ]
