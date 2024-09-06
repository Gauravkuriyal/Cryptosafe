"""
URL configuration for Cryptosafe project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('store/', views.store),
    path('store/otp/', views.store_otp),
    path('store/otp/key/', views.store_key),
    path('fetch/', views.fetch),
    path('about_us/', views.about_us),
    path('feedback/', views._feedback),
    path('why_us/', views.why_us),
    path('faq/', views.faq),
    path('contact_us/', views.contact_us),
    path('delete/', views.delete),
    path('test/', views.test),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)