from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mock_app.urls')),
    # Agrega más URL según sea necesario
]
