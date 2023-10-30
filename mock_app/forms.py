from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


class CustomAuthenticationForm(AuthenticationForm):
    # Agregar campos personalizados si es necesario

    def clean(self):
        # Realizar validaciones personalizadas
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user is None:
                raise forms.ValidationError(
                    'Las credenciales son incorrectas. Por favor, inténtalo de nuevo.')

            return cleaned_data
