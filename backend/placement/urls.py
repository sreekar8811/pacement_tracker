
from django.contrib import admin
from django.urls import path, include
from users.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('api/users/', include('users.urls')),
]
