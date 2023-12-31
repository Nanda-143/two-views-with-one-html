"""
URL configuration for models22 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Topic_insert/',Topic_insert,name='Topic_insert'),
    path('Webpage_insert/',Webpage_insert,name='Webpage_insert'),
    path('Access_insert/',Access_insert,name='Access_insert'),
    path('display_Topic/',display_Topic,name='display_Topic'),
    path('display_Webpage/',display_Webpage,name='display_Webpage'),
    path('display_Access/',display_Access,name='display_Access'),
    path('insert_Topic/',insert_Topic,name='insert_Topic'),
    path('insert_Webpage/',insert_Webpage,name='insert_Webpage'),
    path('insert_Access/',insert_Access,name='insert_Access'),


]
