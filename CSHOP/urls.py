"""CSHOP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from . import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # CHIEN : dòng lệnh dưới sẽ đi đến file store.urls -> index trong view -> thực hiện hàm trong view.py
    path('', include('store.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#NHUT: dòng trên set 2 giá trị MEDIA_URL và MEDIA_ROOT để Upload file lên Django

urlpatterns += staticfiles_urlpatterns()