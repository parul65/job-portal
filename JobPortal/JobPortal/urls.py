from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', include('jobs.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # for login/logout
]









