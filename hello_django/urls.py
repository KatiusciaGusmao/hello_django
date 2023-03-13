"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),   # padrão django
    # path('hello/', views.hello),  #nova rota que leva até o método criado no views do core

#url com 1 parametro
    #path('hello/<nome>/', views.hello)

#url com 2 parametros, nome e idade
    # path('hello/<nome>/<int:idade>/', views.hello)

#url com 2 parametros, soma
    path('hello/<numA>/<numB>/', views.hello)

]
