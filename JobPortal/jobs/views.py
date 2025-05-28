from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Job, Application
from .forms import JobForm

def job_list(request):
    jobs = Job.objects.all().order_by('-posted_at')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

@login_required
def apply_for_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    # Check if already applied
    if Application.objects.filter(job=job, user=request.user).exists():
        return render(request, 'jobs/already_applied.html', {'job': job})
    Application.objects.create(job=job, user=request.user)
    return render(request, 'jobs/application_success.html', {'job': job})

@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'jobs/add_job.html', {'form': form})















