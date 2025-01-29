"""
URL configuration for myDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
import myapp.views as myapp_views  # 定義別名以區別後續可能有多個app

urlpatterns = [
    path('admin/', admin.site.urls),

    # myapp.views
    path('myapp/', myapp_views.home),
    path('myapp/hi/<username>/', myapp_views.hiname),      # 傳遞字串參數 username
    path('myapp/age/<int:year>/', myapp_views.age),        # 傳遞數值參數 year
    path('myapp/hello/', myapp_views.hello_view),
    path('myapp/getName/<username>/', myapp_views.getOneByName), # 傳遞字串參數 username
    path('myapp/getAll/', myapp_views.getAll),
    path('myapp/getAll_pd/', myapp_views.getAll_pd),
    path('myapp/templates/', myapp_views.main),     # 模板繼承範例
    path('myapp/login/', myapp_views.login),        # 表單範例
]