"""
URL configuration for hos_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from hospital.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",login_view,name="login"),
    path("register/",register,name="register"),
    path("doc_manage/",doc_manage,name="doc_manage"),
    path("home/",home,name="home"),
    path("doc_view/<int:id>",doc_view,name="doc_view"),
    path("pat_manage/",pat_manage,name="pat_manage"),
    path("pat_view/<int:id>",pat_view,name="pat_view"),
    path("doc_edit/<int:id>",doc_edit,name="doc_edit"),
    path("pat_edit/<int:id>",pat_edit,name="pat_edit"),
    path("apot_manage/",apot_manage,name="apot_manage"),
    path("apot_view/<int:id>",apot_view,name="apot_view"),
    path("apot_edit/<int:id>",apot_edit,name="apot_edit"),
    path("logout/",logout_view,name="logout"),
    path("doc_del/<int:id>",doc_del,name="doc_del"),
    path("pat_del/<int:id>",pat_del,name="pat_del"),
    path("apot_done/<int:id>",apot_done,name="apot_done"),
    path("profile/",profile,name="profile"),
    path("updt_prof/",updt_prof,name="updt_prof")
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)