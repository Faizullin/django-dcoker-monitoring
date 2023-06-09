"""monitoring URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect, render
from django.urls import reverse

def redirect_to_dashboard(request):
    return redirect(reverse('dashboard:index'))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/auth/', include('dashboard_authentication.urls',namespace='dashboard_auth')),
    path('dashboard/', include('dashboard.urls',namespace='dashboard')),
    path('dashboard/drive/', include('storage_drive.urls',namespace='storage_drive')),
    path('api/dashboard/', include('dashboard_api.urls',namespace='dashboard_api')),
    path('', redirect_to_dashboard)
]

def page_not_found_view(request, exception):
    return render(request, 'dashboard/page-404.html', status=404)

handler404 = page_not_found_view

#if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)