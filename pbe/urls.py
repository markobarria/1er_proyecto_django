from django.contrib import admin
from django.urls import path
from pbe.views import bienvenida, calcula_edad

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenida),
    path ('edad/<int:edad>', calcula_edad),
    
]
