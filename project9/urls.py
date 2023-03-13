"""project9 URL Configuration

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
from app1.views import *
from app2.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jinja_print1/',jinja_print1,name='jinja_print1'),
    path('jinja_print2/',jinja_print2,name='jinja_print2'),
    path('jinja_first1/',jinja_first1,name='jinja_first1'),
    path('jinja_first2/',jinja_first2,name='jinja_first2'),
]
