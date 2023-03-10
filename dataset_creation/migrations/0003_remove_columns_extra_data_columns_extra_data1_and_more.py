# Generated by Django 4.0.5 on 2023-03-04 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset_creation', '0002_alter_columns_extra_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='columns',
            name='extra_data',
        ),
        migrations.AddField(
            model_name='columns',
            name='extra_data1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='columns',
            name='extra_data2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='schemas',
            name='column_separator',
            field=models.CharField(choices=[(',', 'Comma (,)'), (';', 'Semicolon (;)')], default=(',', 'Comma (,)'), max_length=255),
        ),
        migrations.AddField(
            model_name='schemas',
            name='string_character',
            field=models.CharField(choices=[("'", 'Double-quote (")'), ('"', "Single-quote (')")], default=("'", 'Double-quote (")'), max_length=255),
        ),
    ]
