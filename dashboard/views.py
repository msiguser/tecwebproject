from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required
def init(request):
    return render(request, 'dashboard/index.html')

@login_required
def list(request):
    return render(request, 'dashboard/dashboard_list.html')