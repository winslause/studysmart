from django.contrib import admin
from .models import Document, Question, PerformanceMetric

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'upload_date')
    list_filter = ('page', 'upload_date')
    search_fields = ('title', 'description', 'tags')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_by', 'page', 'created_at')
    list_filter = ('page', 'posted_by')
    search_fields = ('title', 'description')

@admin.register(PerformanceMetric)
class PerformanceMetricAdmin(admin.ModelAdmin):
    list_display = ('question_count', 'avg_load_time', 'last_updated')
    readonly_fields = ('last_updated',)