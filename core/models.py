# models.py
from django.db import models
from .validators import validate_file_type, validate_file_size
from django.contrib.auth.models import User as AuthUser

# Custom User model (unchanged)
class User(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.username

# Define your Page categories
PAGE_CHOICES = [
    ('index', 'Index Page'),
    ('about', 'About Page'),
    ('services', 'Services Page'),
    ('register', 'Register Page'),
    ('reports', 'Reports Page'),
    ('computer_science', 'computer_science Page'),
    ('machine_learning', 'machine_learning Page'),
    ('economics', 'Economics Page'),
    ('data_analysis', 'Data Analysis Page'),
    ('data_mining', 'Data Mining Page'),
    ('finance', 'Finance Page'),
    ('business_analytics', 'Business Analytics Page'),
    ('case_studies', 'Case Studies Page'),
    ('business', 'Business Page'),
    ('marketing', 'Marketing Page'),
    ('research', 'Research Page'),
    ('past_solutions', 'Past Solutions Page'),
]

class Document(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='documents/', validators=[validate_file_size, validate_file_type])
    upload_date = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    page = models.CharField(max_length=50, choices=PAGE_CHOICES, default='index')

    def __str__(self):
        return self.title

class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    page = models.CharField(max_length=50, choices=PAGE_CHOICES, default='past_solutions')
    document = models.ForeignKey(Document, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

class PerformanceMetric(models.Model):
    question_count = models.IntegerField(default=0)
    avg_load_time = models.FloatField(default=0.0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Metrics updated on {self.last_updated}"