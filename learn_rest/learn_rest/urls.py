from django.contrib import admin
from django.urls import path,include;

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
    path('apis/auth',include('rest_framework.urls')),
]
