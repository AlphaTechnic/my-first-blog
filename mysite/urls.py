from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('blog.urls')),
    path(r'^accounts/login/$', views.login, name='login'),
    path(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    path(r'', include('blog.urls')),
]
