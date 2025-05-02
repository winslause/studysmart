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
    logger.debug(f"Index page rendered with {documents.count()} documents")
    return render(request, 'index.html', {'documents': documents})

def about(request):
    documents = Document.objects.filter(page='about')
    logger.debug(f"About page rendered with {documents.count()} documents")
    return render(request, 'about.html', {'documents': documents})

def services(request):
    documents = Document.objects.filter(page='services')
    logger.debug(f"Services page rendered with {documents.count()} documents")
    return render(request, 'services.html', {'documents': documents})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            logger.info(f"User registered: {username}")
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
        else:
            logger.warning(f"Registration failed: {form.errors}")
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
            logger.info(f"User logged in: {username}")
            next_url = request.GET.get('next', 'index')
            return redirect(next_url)
        else:
            logger.warning(f"Login failed for username: {username}")
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def reports(request):
    documents = Document.objects.filter(page='reports')
    logger.debug(f"Reports page rendered with {documents.count()} documents")
    return render(request, 'reports.html', {'documents': documents})

def computer_science(request):
    documents = Document.objects.filter(page='computer_science')
    logger.debug(f"Computer Science page rendered with {documents.count()} documents")
    return render(request, 'cs.html', {'documents': documents})

def machine_learning(request):
    documents = Document.objects.filter(page='machine_learning')
    logger.debug(f"Machine Learning page rendered with {documents.count()} documents")
    return render(request, 'ml.html', {'documents': documents})

def economics(request):
    documents = Document.objects.filter(page='economics')
    logger.debug(f"Economics page rendered with {documents.count()} documents")
    return render(request, 'economics.html', {'documents': documents})

def data_analysis(request):
    documents = Document.objects.filter(page='data_analysis')
    logger.debug(f"Data Analysis page rendered with {documents.count()} documents")
    return render(request, 'data_analysis.html', {'documents': documents})

def data_mining(request):
    documents = Document.objects.filter(page='data_mining')
    logger.debug(f"Data Mining page rendered with {documents.count()} documents")
    return render(request, 'data_mining.html', {'documents': documents})

def finance(request):
    documents = Document.objects.filter(page='finance')
    logger.debug(f"Finance page rendered with {documents.count()} documents")
    return render(request, 'finance.html', {'documents': documents})

def business_analytics(request):
    documents = Document.objects.filter(page='business_analytics')
    logger.debug(f"Business Analytics page rendered with {documents.count()} documents")
    return render(request, 'business_analytics.html', {'documents': documents})

def case_studies(request):
    documents = Document.objects.filter(page='case_studies')
    logger.debug(f"Case Studies page rendered with {documents.count()} documents")
    return render(request, 'case_studies.html', {'documents': documents})

def business(request):
    documents = Document.objects.filter(page='business')
    logger.debug(f"Business page rendered with {documents.count()} documents")
    return render(request, 'business.html', {'documents': documents})

def marketing(request):
    documents = Document.objects.filter(page='marketing')
    logger.debug(f"Marketing page rendered with {documents.count()} documents")
    return render(request, 'marketing.html', {'documents': documents})

def research(request):
    documents = Document.objects.filter(page='research')
    logger.debug(f"Research page rendered with {documents.count()} documents")
    return render(request, 'research.html', {'documents': documents})

def technical_writing(request):
    logger.debug("Technical Writing page rendered")
    return render(request, 'technical_writing.html', {})

def exams(request):
    logger.debug("Exams page rendered")
    return render(request, 'exams.html', {})

def assignment(request):
    logger.debug("Assignment page rendered")
    return render(request, 'assignment.html', {})

def past_solutions(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            logger.warning("Unauthorized POST attempt to past_solutions by unauthenticated user")
            messages.error(request, 'You must be logged in to post a question.')
            return redirect('login')
        
        action = request.POST.get('action')
        logger.debug(f"POST action received in past_solutions: {action}, POST data: {request.POST}")
        if action == 'post_question':
            title = request.POST.get('title')
            description = request.POST.get('description')
            page = request.POST.get('page')
            document = request.FILES.get('document')
            image = request.FILES.get('image')

            if title and description and page:
                try:
                    question = Question(
                        title=title,
                        description=description,
                        posted_by=request.user,
                        page=page
                    )
                    if document:
                        doc = Document(
                            title=f"Document for {title}",
                            file=document,
                            page=page
                        )
                        doc.save()
                        question.document = doc
                    if image:
                        question.image = image
                    question.save()
                    logger.info(f"Question posted by {request.user.username}: ID={question.id}, Title={title}, Page={page}")
                    messages.success(request, 'Question posted successfully!')
                except Exception as e:
                    logger.error(f"Error posting question in past_solutions: {str(e)}")
                    messages.error(request, f'Error posting question: {str(e)}')
            else:
                logger.warning("Missing required fields for posting question")
                messages.error(request, 'Title, description, and page are required.')
            return redirect('past_solutions')

    questions = Question.objects.filter(page='past_solutions').order_by('-created_at')
    logger.debug(f"Past solutions rendered with {questions.count()} questions")
    return render(request, 'past_solutions.html', {
        'questions': questions,
        'PAGE_CHOICES': PAGE_CHOICES
    })

def logout_view(request):
    logger.info(f"User logged out: {request.user.username if request.user.is_authenticated else 'Anonymous'}")
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_portal(request):
    questions = Question.objects.all().order_by('-created_at')
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
        logger.debug(f"POST action received in admin_portal: {action}, POST data: {request.POST}")
        if action == 'post_question':
            title = request.POST.get('title')
            description = request.POST.get('description')
            page = request.POST.get('page', 'past_solutions')
            document = request.FILES.get('document')
            image = request.FILES.get('image')

            if title and description:
                try:
                    question = Question(
                        title=title,
                        description=description,
                        posted_by=request.user,
                        page=page
                    )
                    if document:
                        doc = Document(
                            title=f"Document for {title}",
                            file=document,
                            page=page
                        )
                        doc.save()
                        question.document = doc
                    if image:
                        question.image = image
                    question.save()
                    logger.info(f"Question posted by {request.user.username}: ID={question.id}, Title={title}, Page={page}")
                    messages.success(request, 'Question posted successfully!')
                except Exception as e:
                    logger.error(f"Error posting question in admin_portal: {str(e)}")
                    messages.error(request, f'Error posting question: {str(e)}')
            else:
                logger.warning("Missing required fields for posting question")
                messages.error(request, 'Title and description are required.')
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
                if question.document:
                    question.document.delete()
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
                logger.info(f"Password changed for user {request.user.username}")
                messages.success(request, 'Password changed successfully!')
            else:
                logger.warning(f"Password change failed for user {request.user.username}: {form.errors}")
                messages.error(request, 'Password change failed. Please check your inputs.')
            return redirect('admin_portal')

    logger.debug(f"Admin portal rendered with {questions.count()} questions")
    return render(request, 'admin_portal.html', {
        'questions': questions,
        'metric': metric,
        'question_page_choices': PAGE_CHOICES
    })