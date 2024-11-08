"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.views.generic import ListView, DetailView, TemplateView
from product.models import AmazonProduct
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', ListView.as_view(
        model=AmazonProduct,
        template_name='product/list.html',
        context_object_name='products'
    ), name='home'),
    path('<int:pk>/', DetailView.as_view(
        model=AmazonProduct,
        template_name='product/detail.html',
        context_object_name='product'
    ), name='product_detail'),
    path('about/', TemplateView.as_view(
        template_name='about/about.html'
    ), name='about'),
    path('about/privacy-policy/', TemplateView.as_view(
        template_name='about/privacy-policy.html'
    ), name='privacy_policy'),
    path('about/terms-of-use/', TemplateView.as_view(
        template_name='about/terms-of-use.html'
    ), name='terms_of_use'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)