from django.db import models
from django.conf import settings


class Schemas(models.Model):
    title = models.CharField(
        max_length=225,
    )
    column_separator = models.CharField(
        max_length=255,
        choices=((",", "Comma (,)"),
                 (';', "Semicolon (;)")),
        default=(",", "Comma (,)")
    )
    string_character = models.CharField(
        max_length=255,
        choices=(("\'", "Double-quote (\")"),
                 ('\"', "Single-quote (\')")),
        default=("\'", "Double-quote (\")")
    )
    modified_at = models.DateField(
        auto_now=True
    )
    user_creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Columns(models.Model):
    data_types = (
        ('full_name', 'Full Name'),
        ('job', 'Job'),
        ('email', 'Email'),
        ('domain_name', 'Domain Name'),
        ('phone_number', 'Phone Number'),
        ('company_name', 'Company Name'),
        ('text', 'Text'),
        ('integer', 'Integer'),
        ('address', 'Address'),
        ('date', 'Date'),
    )
    column_name = models.CharField(max_length=255)
    data_type = models.CharField(max_length=20, choices=data_types)
    data_schema = models.ForeignKey(Schemas, on_delete=models.CASCADE)
    extra_data1 = models.CharField(max_length=255, blank=True, null=True)
    extra_data2 = models.CharField(max_length=255, blank=True, null=True)


class FakeData(models.Model):

    schema = models.ForeignKey(Schemas, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now=True)
    csv_file = models.FileField(upload_to='media/', blank=True)

