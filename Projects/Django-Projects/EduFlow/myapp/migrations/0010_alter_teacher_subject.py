# Generated by Django 4.1 on 2023-04-15 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_teacher_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.subject'),
        ),
    ]