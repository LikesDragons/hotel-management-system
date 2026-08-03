from django.shortcuts import render

def guest_dashboard(request):
    return render(request,
                  "guest_management/guest_dashboard.html")