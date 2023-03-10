import csv
from random import randint

from django.core.files.base import ContentFile
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.views import View
from faker import Faker

from dataset_creation.models import Columns, Schemas, FakeData
from .forms import NumberForm


class GenerationManageView(View):
    template_name = 'csv_generation/csv_manage.html'

    def get(self, request, pk):
        columns = Columns.objects.filter(data_schema_id=pk)
        number_form = NumberForm()
        generated_data = FakeData.objects.filter(schema_id=pk)
        return render(request, self.template_name, {'columns': columns,
                                                    'number_form': number_form,
                                                    'generated_data': generated_data,
                                                    'pk': pk,
                                                    'page_title': 'Data generation'})

    def post(self, request, pk=None):
        if pk is None:
            pk = request.POST.get('pk')
            pk = int(pk)
        columns = Columns.objects.filter(data_schema_id=pk)
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            rows_number = request.POST.get('rows_number')
            rows_number = int(rows_number.split('=')[2])
            new_data = FakeData()
            new_data.schema_id = pk
            new_data.save()
            column_types = {}
            for column in columns:
                key = column.column_name
                if column.data_type == 'integer' or column.data_type == 'text':
                    value = [column.data_type, int(column.extra_data1), int(column.extra_data2)]
                else:
                    value = column.data_type
                column_types[key] = value
            csv_data = self.generate_fake_csv(column_types,
                                              rows_number,
                                              Schemas.objects.get(id=pk).column_separator,
                                              Schemas.objects.get(id=pk).string_character)
            new_data.csv_file.save(f'{new_data.id}.csv', ContentFile(csv_data))
            new_data.save()
            return JsonResponse({'status': 'Success', 'pk': new_data.id})

    def generate_fake_csv(self, column_types, num_records, separator, raw_sep):
        column_names = list(column_types.keys())
        data = [column_names]
        fake = Faker()
        for i in range(num_records - 1):
            row = []

            for column_type in column_types.values():
                if isinstance(column_type, list) and column_type[0] == 'integer':
                    row.append(randint(column_type[1], column_type[2]))
                elif isinstance(column_type, list) and column_type[0] == 'text':
                    text = fake.text(max_nb_chars=column_type[2])
                    while len(text) < column_type[1]:
                        text = fake.text(max_nb_chars=column_type[2])
                    row.append(text)
                elif column_type == 'full_name':
                    row.append(fake.name())
                elif column_type == 'job':
                    row.append(fake.job())
                elif column_type == 'email':
                    row.append(fake.email())
                elif column_type == 'phone_number':
                    row.append(fake.phone_number())
                elif column_type == 'company_name':
                    row.append(fake.company())
                elif column_type == 'domain_name':
                    row.append(fake.domain_name())
                elif column_type == 'address':
                    row.append(fake.address())
                elif column_type == 'date':
                    row.append(fake.date())
            data.append(row)
        csv_data = []
        for row in data:
            csv_data.append(raw_sep + separator.join(str(cell).replace(separator,
                                                                       '').replace('"', '').replace("'", '') for cell
                                                     in row) + raw_sep)
        csv_data = '\n'.join(csv_data)
        return csv_data


def download_file(request, pk):
    file = get_object_or_404(FakeData, pk=pk)
    file_data = file.csv_file.read()
    response = HttpResponse(file_data, content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file.csv_file.name)
    return response
