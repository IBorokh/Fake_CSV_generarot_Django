from django import forms
from django.forms import BaseModelFormSet

from . import models


class SchemaForm(forms.ModelForm):

    class Meta:
        model = models.Schemas
        fields = ["title", "column_separator", "string_character"]


class ColumnForm(forms.ModelForm):
    extra_data1 = forms.IntegerField(label='From', required=False)
    extra_data2 = forms.IntegerField(label='To', required=False)

    class Meta:
        model = models.Columns
        fields = ['column_name', 'data_type', 'extra_data1', 'extra_data2']

    def clean(self):
        cleaned_data = super().clean()
        extra_data1 = cleaned_data.get("extra_data1")
        extra_data2 = cleaned_data.get("extra_data2")

        if extra_data1 is not None and extra_data2 is not None and extra_data1 > extra_data2:
            raise forms.ValidationError("Min value must be less than max value")



