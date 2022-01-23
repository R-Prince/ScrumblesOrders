from django.shortcuts import render


def dashboard(request):
    # A view to return dashboard
    return render(request, 'dashboard/dashboard.html')
