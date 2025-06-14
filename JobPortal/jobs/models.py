from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Job(models.Model):
    JOB_TYPE_CHOICES = (
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Internship', 'Internship'),
        ('Contract', 'Contract'),
    )

    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES)
    salary = models.IntegerField(null=False)  # or null=True?


    description = models.TextField()

    def __str__(self):
        return self.title

class Application(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    cover_letter = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.job.title}"














