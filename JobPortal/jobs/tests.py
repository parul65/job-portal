from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50, choices=[('FT', 'Full-Time'), ('PT', 'Part-Time')])
    salary = models.IntegerField()

    def __str__(self):
        return self.title

