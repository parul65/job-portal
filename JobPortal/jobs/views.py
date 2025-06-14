from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Job, Application


# ========================
# User Login View
# ========================
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and not user.is_staff:
            login(request, user)
            return redirect('user_dashboard')
        else:
            return render(request, 'jobs/login.html', {'error': 'Invalid credentials'})
    return render(request, 'jobs/login.html')


# ========================
# Admin Login View
# ========================
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        admin = authenticate(request, username=username, password=password)
        if admin is not None and admin.is_staff:
            login(request, admin)
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid credentials or not an admin account.")
    return render(request, 'jobs/admin_login.html')


# ========================
# User Dashboard
# ========================
@login_required
@user_passes_test(lambda u: not u.is_staff)
def user_dashboard(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'jobs/user_dashboard.html', {'applications': applications})


# ========================
# Admin Dashboard
# ========================
@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/admin_dashboard.html', {'jobs': jobs})


# ========================
# Job List View
# ========================
def job_list(request):
    search_query = request.GET.get('search', '')
    company_query = request.GET.get('company', '')

    jobs = Job.objects.all()

    if search_query:
        jobs = jobs.filter(title__icontains=search_query)
    if company_query:
        jobs = jobs.filter(company__name__icontains=company_query)

    return render(request, 'jobs/job_list.html', {'jobs': jobs})


# ========================
# Apply for Job View
# ========================
@login_required
@user_passes_test(lambda u: not u.is_staff)
def apply_for_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if Application.objects.filter(user=request.user, job=job).exists():
        messages.info(request, "You have already applied for this job.")
        return redirect('job_list')

    if request.method == 'POST':
        resume = request.FILES.get('resume')
        cover_letter = request.POST.get('cover_letter')

        Application.objects.create(
            user=request.user,
            job=job,
            resume=resume,
            cover_letter=cover_letter
        )

        messages.success(request, f"You have successfully applied for {job.title}.")
        return redirect('job_list')

    return render(request, 'jobs/apply.html', {'job': job})


# ========================
# Add Job View (Admin Only)
# ========================
@login_required
@user_passes_test(lambda u: u.is_staff)
def add_job(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        location = request.POST['location']
        company = request.POST['company']
        salary = request.POST['salary']

        Job.objects.create(
            title=title,
            description=description,
            location=location,
            company=company,
            salary=salary
        )

        messages.success(request, "Job added successfully.")
        return redirect('admin_dashboard')

    return render(request, 'jobs/add_job.html')




















