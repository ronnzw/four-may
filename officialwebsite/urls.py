"""officialwebsite URL Configuration

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

from settings import base, local

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('address/', include('address.urls')),
    path('currencies/', include('currencies.urls'))
]

admin.site.site_header = '4May Admnistration Panel'
admin.site.site_title = '4May'


if local.DEBUG:
    urlpatterns = urlpatterns + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
