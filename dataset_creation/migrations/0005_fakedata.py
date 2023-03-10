# Generated by Django 4.0.5 on 2023-03-08 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataset_creation', '0004_remove_columns_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='FakeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now=True)),
                ('csv_file', models.FileField(blank=True, upload_to='media/')),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataset_creation.schemas')),
            ],
        ),
    ]