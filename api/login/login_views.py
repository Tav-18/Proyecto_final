from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Vista para iniciar sesión
def login_views(request):
    template_name = "login.html"

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Autenticar usuario
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)  # Inicia sesión
            return redirect("index")  # Redirige a la página principal
        else:
            # Mostrar mensaje de error si las credenciales son incorrectas
            messages.error(request, "Credenciales incorrectas. Por favor, inténtalo de nuevo.")
    
    return render(request, template_name)


# Vista para registrar usuario
def register_views(request):
    template_name = "register.html"

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm-password")

        # Validar campos
        if password != confirm_password:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, template_name)

        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
            return render(request, template_name)

        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo electrónico ya está registrado.")
            return render(request, template_name)

        # Crear usuario si las validaciones pasan
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Usuario registrado exitosamente. Ahora puedes iniciar sesión.")
        return redirect("login")  # Redirigir al login
    
    return render(request, template_name)

def forgot_views(request):
    template_name = "forgot.html"

    if request.method == "POST":
        email = request.POST.get("email")

        # Validar si el correo existe
        if User.objects.filter(email=email).exists():
            messages.success(request, "Se ha enviado un enlace de recuperación a tu correo.")
        else:
            messages.error(request, "El correo ingresado no está registrado.")

    return render(request, template_name)