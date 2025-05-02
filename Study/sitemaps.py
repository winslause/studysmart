from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['index', 'about', 'services', 'past_solutions', 'register', 'login']
    def location(self, item):
        return reverse(item)

class CoreSitemap(Sitemap):
    def items(self):
        return ['computer_science', 'machine_learning', 'economics', 'data_analysis', 'data_mining', 'finance', 'business_analytics', 'case_studies', 'business', 'marketing', 'research', 'technical_writing', 'exams', 'assignment']
    def location(self, item):
        return reverse(item)