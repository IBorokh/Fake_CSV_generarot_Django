from django.urls import path
from . import views


app_name = 'dataset_creation'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('create_schema/', views.SchemaManageView.as_view(), name='schema_create'),
    path('schema/<int:pk>/update', views.SchemaManageView.as_view(), name='schema_update'),
    path('schema/<int:pk>/delete', views.SchemaDeleteView.as_view(), name='schema_delete')
]
