from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from jobs import views as job_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Job-related routes
    path('jobs/', include('jobs.urls')),

    # User login/logout
    path('user/login/', job_views.user_login, name='user_login'),
    path('admin/login/', job_views.admin_login, name='admin_login'),

    # Dashboards
    path('user/dashboard/', job_views.user_dashboard, name='user_dashboard'),
    path('admin/dashboard/', job_views.admin_dashboard, name='admin_dashboard'),
]

# Serve media files during development (e.g. resumes)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Optional: Set default redirect for login-required decorators
from django.conf import settings
from django.contrib.auth import views as auth_views

# This will prevent Django from trying to redirect to /accounts/login/
settings.LOGIN_URL = '/user/login/'










