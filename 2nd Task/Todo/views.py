from django.shortcuts import render , redirect
from .forms import SignUpForm ,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile,Task,User1
from django.contrib.auth.hashers import check_password
from django.views.decorators.http import require_POST

# Create your views here.
def home(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

def todo(request):
    return render(request,"todo.html")

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_profile = form.save()
            user1 = User1.objects.create(username=user_profile.email)  # Assuming 'email' is the unique identifier
            user_profile.user1 = user1
            user_profile.save()
            messages.success(request, 'You have signed up successfully!')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST) 
        if form.is_valid():
            email = form.cleaned_data.get('email') 
            password = form.cleaned_data.get('password')
            print(f"Email: {email}, Password: {password}")
            
            user = authenticate(request, username=email, password=password)

            if user is not None:
                # Login successful
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('todo.html')  # Replace 'home' with your desired redirect path
            else:
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def todo_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo.html', {'tasks': tasks})

@require_POST
def add_task(request):
    task_text = request.POST['task_text']
    task_status = request.POST['task_status']
    Task.objects.create(task_text=task_text, task_status=task_status)
    return redirect('todo')    