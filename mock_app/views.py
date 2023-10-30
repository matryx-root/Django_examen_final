from django.shortcuts import render, redirect
from .models import Producto
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import CustomAuthenticationForm


def lista_productos(request):

    productos = Producto.objects.all()

    nombre = request.GET.get('nombre')
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')
    stock_min = request.GET.get('stock_min')
    empresa = request.GET.get('empresa')

    if nombre:
        productos = productos.filter(nombre__icontains=nombre)

    if precio_min:
        productos = productos.filter(precio_unidad__gte=precio_min)

    if precio_max:
        productos = productos.filter(precio_unidad__lte=precio_max)

    if stock_min:
        productos = productos.filter(stock__gte=stock_min)

    if empresa:
        productos = productos.filter(id_proveedor__empresa=empresa)

    # context = {
    #     'productos': productos,
    # }

    # Obtener el nombre de usuario actual
    username = request.user.username

    # Obtener la hora de ingreso actual
    hora_ingreso = timezone.now()

    # Actualizar la cuenta de accesos
    if 'access_count' not in request.session:
        request.session['access_count'] = 1
    else:
        request.session['access_count'] += 1

    return render(request, 'mock_app/lista_productos.html', {
        'username': username,
        'hora_ingreso': hora_ingreso,
        'access_count': request.session['access_count'],
        'productos': productos,  # Asegúrate de incluir los productos como lo hacías antes
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirige a la página principal después del registro
            return redirect('inicio_sesion')
    else:
        form = UserCreationForm()
    return render(request, 'mock_app/registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Redirige a la página principal después del inicio de sesión
            return redirect('lista_productos')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'mock_app/inicio_sesion.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('lista_productos')


def login_redirect(request):
    return redirect('inicio_sesion')
