# Generated by Django 4.1 on 2023-04-15 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_subject_teacher_id_alter_teacher_subject_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='subject_id',
            new_name='subject',
        ),
    ]