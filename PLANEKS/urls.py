from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dataset_creation.urls', namespace='datasets')),
    path('login/', include('login.urls', namespace='login')),
    path('generate_csv/', include('csv_generation.urls', namespace='csv'))
]
