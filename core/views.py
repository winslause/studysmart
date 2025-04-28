from django.shortcuts import render, redirect
from .models import Document, Question, PerformanceMetric, PAGE_CHOICES
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ObjectDoesNotExist
import logging

# Set up logging
logger = logging.getLogger(__name__)

def index(request):
    documents = Document.objects.filter(page='index')
    return render(request, 'index.html', {'documents': documents})

def about(request):
    documents = Document.objects.filter(page='about')
    return render(request, 'about.html', {'documents': documents})

def services(request):
    documents = Document.objects.filter(page='services')
    return render(request, 'services.html', {'documents': documents})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_portal')
            else:
                return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def reports(request):
    documents = Document.objects.filter(page='reports')
    return render(request, 'reports.html', {'documents': documents})

def cs(request):
    documents = Document.objects.filter(page='cs')
    return render(request, 'cs.html', {'documents': documents})

def ml(request):
    documents = Document.objects.filter(page='ml')
    return render(request, 'ml.html', {'documents': documents})

def economics(request):
    documents = Document.objects.filter(page='economics')
    return render(request, 'economics.html', {'documents': documents})

def data_analysis(request):
    documents = Document.objects.filter(page='data_analysis')
    return render(request, 'data_analysis.html', {'documents': documents})

def data_mining(request):
    documents = Document.objects.filter(page='data_mining')
    return render(request, 'data_mining.html', {'documents': documents})

def finance(request):
    documents = Document.objects.filter(page='finance')
    return render(request, 'finance.html', {'documents': documents})

def business_analytics(request):
    documents = Document.objects.filter(page='business_analytics')
    return render(request, 'business_analytics.html', {'documents': documents})

def case_studies(request):
    documents = Document.objects.filter(page='case_studies')
    return render(request, 'case_studies.html', {'documents': documents})

def business(request):
    documents = Document.objects.filter(page='business')
    return render(request, 'business.html', {'documents': documents})

def marketing(request):
    documents = Document.objects.filter(page='marketing')
    return render(request, 'marketing.html', {'documents': documents})

def research(request):
    documents = Document.objects.filter(page='research')
    return render(request, 'research.html', {'documents': documents})

def technical_writing(request):
    return render(request, 'technical_writing.html', {})

def exams(request):
    return render(request, 'exams.html', {})

def assignment(request):
    return render(request, 'assignment.html', {})

def past_solutions(request):
    questions = Question.objects.filter(page='past_solutions').order_by('-created_at')
    return render(request, 'past_solutions.html', {'questions': questions})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_portal(request):
    questions = Question.objects.filter(page='past_solutions').order_by('-created_at')
    # Get or create single PerformanceMetric object
    metric, created = PerformanceMetric.objects.get_or_create(id=1, defaults={
        'question_count': 0,
        'avg_load_time': 0.0,
        'last_updated': timezone.now()
    })
    metric.question_count = Question.objects.count()
    metric.avg_load_time = 1.5  # Placeholder
    metric.last_updated = timezone.now()
    metric.save()

    if request.method == 'POST':
        action = request.POST.get('action')
        logger.debug(f"POST action received: {action}, POST data: {request.POST}")
        if action == 'post_question':
            title = request.POST.get('title')
            description = request.POST.get('description')
            page = request.POST.get('page', 'past_solutions')
            try:
                Question.objects.create(
                    title=title,
                    description=description,
                    posted_by=request.user,
                    page=page
                )
                messages.success(request, 'Question posted successfully!')
            except Exception as e:
                logger.error(f"Error posting question: {str(e)}")
                messages.error(request, f'Error posting question: {str(e)}')
            return redirect('admin_portal')
        elif action == 'delete_question':
            question_id = request.POST.get('question_id')
            logger.debug(f"Attempting to delete question ID: {question_id}")
            if not question_id:
                logger.error("Delete request failed: question_id is missing")
                messages.error(request, 'Invalid request: Question ID is missing.')
                return redirect('admin_portal')
            try:
                question = Question.objects.get(id=question_id)
                question.delete()
                logger.info(f"Question ID {question_id} deleted by {request.user.username}")
                messages.success(request, 'Question deleted successfully!')
            except ObjectDoesNotExist:
                logger.warning(f"Question ID {question_id} not found")
                messages.error(request, 'Question not found.')
            except Exception as e:
                logger.error(f"Error deleting question ID {question_id}: {str(e)}")
                messages.error(request, f'Error deleting question: {str(e)}')
            return redirect('admin_portal')
        elif action == 'change_password':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password changed successfully!')
            else:
                messages.error(request, 'Password change failed. Please check your inputs.')
            return redirect('admin_portal')

    return render(request, 'admin_portal.html', {
        'questions': questions,
        'metric': metric,
        'question_page_choices': PAGE_CHOICES
    })