from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ComplaintForm
from .models import Complaint
import requests

# Replace with your Hugging Face Space API endpoint
HF_API_URL = "https://sahith22-complaint-classifier.hf.space/predict"

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print("POST data:", request.POST)
        print("Form valid?", form.is_valid())
        print("Form errors:", form.errors)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('file_complaint')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('file_complaint')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def file_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint_text = form.cleaned_data['text']
            # Call Hugging Face API to get category
            try:
                response = requests.post(HF_API_URL, json={"text": complaint_text})
                print("API status:", response.status_code)
                print("API response:", response.text)
                category = response.json().get("category", "Unknown")
            except Exception as e:
                print("API error:", e)
                category = 'credit_card'  # fallback
            Complaint.objects.create(user=request.user, text=complaint_text, category=category)
            return redirect('complaint_list')
    else:
        form = ComplaintForm()
    return render(request, 'complaints/file_complaint.html', {'form': form})

@login_required
def complaint_list(request):
    complaints = Complaint.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'complaints/complaint_list.html', {'complaints': complaints}) 