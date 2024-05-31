import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import RegisterForm, EntryForm
from .models import Entry, SupportMessage
from django.http import JsonResponse


def home_page_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    return render(request, 'home.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def index_view(request):
    entries = Entry.objects.filter(user=request.user).order_by('-created_at')
    support_messages = SupportMessage.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'index.html', {
        'entries': entries,
        'support_messages': support_messages
    })


@login_required
@csrf_exempt
def create_entry(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        content = data.get('content')
        if title and content:
            Entry.objects.create(user=request.user, title=title, content=content)
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'Title and content are required.'})
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})


@login_required
def view_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    return render(request, 'view_entry.html', {'entry': entry})


def edit_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('view_entry', entry_id=entry.id)
    else:
        form = EntryForm(instance=entry)
    return render(request, 'edit_entry.html', {'form': form, 'entry': entry})


def delete_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    if request.method == 'POST':
        entry.delete()
        return redirect('index')
    return render(request, 'delete_entry.html', {'entry': entry})


@csrf_exempt
def send_support_message(request):
    if request.method == 'POST':
        user = request.user
        data = json.loads(request.body)
        message = data.get('message')
        if message:
            SupportMessage.objects.create(user=user, message=message)
            return JsonResponse({'status': 'success'}, status=201)
        else:
            return JsonResponse({'status': 'error', 'message': 'Message cannot be empty.'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)
