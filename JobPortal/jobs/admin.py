from django.contrib import admin
from .models import Company, Job, Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'resume', 'cover_letter', 'status', 'applied_on')
    list_filter = ('status',)
    search_fields = ('user__username', 'job__title')

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'job_type', 'salary')
    search_fields = ('title', 'description', 'company__name')
    list_filter = ('location', 'company', 'job_type')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')











