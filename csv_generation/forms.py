from django import forms


class NumberForm(forms.Form):
    rows = forms.IntegerField(label='Rows', required=True)
