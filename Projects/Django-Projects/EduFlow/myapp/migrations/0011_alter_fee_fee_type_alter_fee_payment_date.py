# Generated by Django 4.1 on 2023-04-22 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_teacher_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='fee_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='fee',
            name='payment_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]