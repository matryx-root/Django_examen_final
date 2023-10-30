from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('inicio-sesion/', views.login_view, name='inicio_sesion'),
    path('registro/', views.register, name='registro'),
    path('cierre-sesion/', views.logout_view, name='cierre_sesion'),
    path('accounts/', include('django.contrib.auth.urls')),

]
