# Generated by Django 3.2.7 on 2023-04-15 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_student_addmission_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='addmission_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='class_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.class'),
        ),
        migrations.AlterField(
            model_name='student',
            name='parent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.parent'),
        ),
    ]
