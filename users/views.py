from django.views.decorators.cache import never_cache
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'El email ya está registrado')
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            messages.success(request, 'Cuenta creada correctamente. Ahora puedes iniciar sesión.')
            return redirect('login')

    return render(request, 'users/register.html')

     

    
@never_cache
def myLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')  # redirige a la vista principal o donde quieras
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'users/login.html')
def logoutView(request):
    """Cerrar sesión del usuario."""
    logout(request)
    return redirect('login')
