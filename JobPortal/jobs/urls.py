from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
    path('add/', views.add_job, name='add_job'),  # This line was missing in your original error
]











