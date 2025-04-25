from django.db import models
from . validators import validate_file_type, validate_file_size


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
    ('cs', 'CS Page'),
    ('ml', 'ML Page'),
    ('economics', 'Economics Page'),
    ('data_analysis', 'Data Analysis Page'),
    ('data_mining', 'Data Mining Page'),
    ('finance', 'Finance Page'),
    ('business_analytics', 'Business Analytics Page'),
    ('case_studies', 'Case Studies Page'),
    ('business', 'Business Page'),
    ('marketing', 'Marketing Page'),
    ('research', 'Research Page'),
]

class Document(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='documents/', validators=[validate_file_size, validate_file_type])
    upload_date = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    page = models.CharField(max_length=50, choices=PAGE_CHOICES, default='index')  # Associate with specific page

    def __str__(self):
        return self.title
