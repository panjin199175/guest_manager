"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from sign import views #导入sign应用views文件

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^$',views.index),
    path('index/', views.index), #添加index/的路径配置
    path('accounts/login/', views.index),
    path('login_action/', views.login_action), #login_action/的登录路径配置
    path('event_manage/', views.event_manage), #event_manage/的发布会管理路径配置
    path('search_name/', views.search_name), #search_name/的发布会管理搜索路径配置
    path('guest_manage/', views.guest_manage), #guest_manage/的发布会管理嘉宾路径配置
    path('search_guest_name/', views.search_guest_name), #search_guest_name/的嘉宾管理搜索路径配置
]
