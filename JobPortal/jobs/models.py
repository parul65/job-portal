from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=255, default='Unknown')
    job_type = models.CharField(max_length=50, choices=[
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Internship', 'Internship'),
        ('Remote', 'Remote'),
    ])
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company.name}"

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=100, null=True, blank=True)
    applicant_email = models.EmailField(null=True, blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    cover_letter = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant_name} applied for {self.job.title}"












