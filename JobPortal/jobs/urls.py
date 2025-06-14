from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),                            # Now it's just /jobs/
    path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
    path('user/login/', views.user_login, name='login'),
    path('user/dashboard/', views.user_dashboard, name='user_dashboard'),
]














