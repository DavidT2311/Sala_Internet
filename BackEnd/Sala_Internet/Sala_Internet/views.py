from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def landing_page(request):
    return render(request, 'Landing/Landing.html')

def validar_admin(request):
    if request.method == 'POST':

        return render(request, 'index.html')
