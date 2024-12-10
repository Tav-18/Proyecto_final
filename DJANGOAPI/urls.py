"""
URL configuration for DJANGOAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.login.login_views import (login_views, 
register_views,forgot_views)
from api.home.home_views import home_views,camera_views
from api.dato_masc.dato_masc_views import guardar_datos_mascota
from api.datos_usu.datos_usu_views import guardar_datos_dueno
from api.chatbot.chatbot_views import chatbot_view



    




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_views, name='login'),
    path('register/', register_views, name='register'),
    path('forgot/', forgot_views, name='forgot'),
    path('home/', home_views, name='home'),
    path('camera/', camera_views, name='camera'),
    path('guardar-dueno/', guardar_datos_dueno, name='guardar_dueno'),
    path('guardar-mascota/', guardar_datos_mascota, name='guardar_mascota'),
    path('datos-usuario/', include('api.datos_usu.urls')),
    path("api/chatbot/", chatbot_view, name="chatbot_view"),
    
]

