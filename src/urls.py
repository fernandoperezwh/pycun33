"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from src.views import (
    sync_view,
    #
    async_view,
    fake_async_view_with_blocking,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sync/', sync_view, name='sync'),
    #
    path('async/', async_view, name='async'),
    path('fake-async/', fake_async_view_with_blocking, name='fake_async_view_with_blocking'),
]
