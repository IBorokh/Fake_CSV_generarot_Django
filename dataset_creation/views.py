from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from .forms import SchemaForm, ColumnForm
from .models import Schemas, Columns
from django.contrib.auth.models import User


class DashboardView(LoginRequiredMixin, View):
    login_url = 'login:signin'
    template_name = 'dataset_creation/dashboard.html'

    def get(self, request):
        schemas = Schemas.objects.filter(user_creator_id=request.user.id)
        return render(request, self.template_name, {'schemas': schemas, 'page_title': 'Dashboard'})


class SchemaManageView(LoginRequiredMixin, View):
    login_url = 'login:signin'
    template_name = 'dataset_creation/schema_manage.html'

    def get(self, request, pk=None):
        if pk:
            schema_form = SchemaForm(instance=Schemas.objects.get(id=pk))
            column_formset = modelformset_factory(Columns,
                                                  form=ColumnForm,
                                                  can_order=True,
                                                  extra=1,
                                                  can_delete=True)(
                queryset=Columns.objects.filter(data_schema_id=pk))
        else:
            schema_form = SchemaForm()
            column_formset = modelformset_factory(Columns,
                                                  form=ColumnForm,
                                                  can_order=True,
                                                  extra=1,
                                                  can_delete=True)(
                queryset=Columns.objects.none())
        return render(request, self.template_name, {"schema_form": schema_form,
                                                    "column_formset": column_formset,
                                                    'page_title': 'Schema manage'})

    def post(self, request, pk=None):
        if pk:
            schema_form = SchemaForm(request.POST, instance=Schemas.objects.get(id=pk))
            column_formset = modelformset_factory(Columns,
                                                  form=ColumnForm,
                                                  can_order=True,
                                                  extra=1,
                                                  can_delete=True)(request.POST,
                                                                   queryset=Columns.objects.filter(
                                                                       data_schema_id=pk))
        else:
            schema_form = SchemaForm(request.POST)
            column_formset = modelformset_factory(Columns,
                                                  form=ColumnForm,
                                                  can_order=True,
                                                  extra=1,
                                                  can_delete=True)(request.POST)

        if schema_form.is_valid() and column_formset.is_valid():
            schema = schema_form.save(commit=False)
            schema.user_creator = User.objects.get(id=request.user.id)
            schema.save()
            columns = column_formset.save(commit=False)
            for column in columns:
                column.data_schema = Schemas.objects.get(id=schema.id)
                column.save()
            column_formset.save()
            return redirect(reverse_lazy('datasets:dashboard'))
        else:
            return render(request, self.template_name, {"schema_form": schema_form, "column_formset": column_formset})


class SchemaDeleteView(LoginRequiredMixin, View):
    login_url = 'login:signin'
    template_name = 'dataset_creation/delete_schema_confirmation.html'

    def get(self, request, pk):
        schema = get_object_or_404(Schemas, id=pk)
        return render(request, self.template_name, {'schema': schema})

    def post(self, request, pk):
        schema = get_object_or_404(Schemas, id=pk)
        schema.delete()
        return redirect(reverse_lazy('datasets:dashboard'))
