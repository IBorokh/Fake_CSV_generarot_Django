from django.urls import path
from .views import GenerationManageView, download_file

app_name = 'csv'

urlpatterns = [
    path('<int:pk>/', GenerationManageView.as_view(), name='manage'),
    path('download/<int:pk>/', download_file, name='download')
]
