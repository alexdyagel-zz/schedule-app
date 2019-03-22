from django.shortcuts import render


def index(request):
    return render(request, 'main_app/start_page.html')


def train(request):
    return render(request, 'main_app/start_page.html')


def bus(request):
    return render(request, 'main_app/start_page.html')
