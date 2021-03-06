"""DonationManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from donation.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('all_logins',all_logins,name='all_logins'),
    path('donor_login',donor_login,name='donor_login'),
    path('charfo_login',charfo_login,name='charfo_login'),
    path('admin_login',admin_login,name='admin_login'),
    path('donor_reg',donor_reg,name='donor_reg'),
    path('charfo_reg',charfo_reg,name='charfo_reg'),
    path('donor_home',donor_home,name='donor_home'),
    path('logout/',Logout,name='logout'),
    path('donate_now',donate_now,name='donate_now')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
