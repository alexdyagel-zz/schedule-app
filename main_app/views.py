from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render

from main_app.models import BusFlight, TrainFlight


def index(request):
    return render(request, 'main_app/start_page.html')


def train(request):
    return render(request, 'main_app/start_page.html')


def bus(request):
    return render(request, 'main_app/start_page.html')


def json_example_bus(request):
    return render(request, 'main_app/json_example.html')


def json_example_train(request):
    return render(request, 'main_app/json_example.html')


def chart_data_bus(request):
    dataset = BusFlight.objects \
        .values('destination') \
        .exclude(destination='') \
        .annotate(total=Count('destination')) \
        .order_by('destination')

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Popular Destinations'},
        'series': [{
            'name': 'count of flights',
            'data': list(map(lambda row: {'name': row['destination'], 'y': row['total']}, dataset))
        }]
    }

    return JsonResponse(chart)


def chart_data_train(request):
    dataset = TrainFlight.objects \
        .values('destination') \
        .exclude(destination='') \
        .annotate(total=Count('destination')) \
        .order_by('destination')

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Popular Destinations'},
        'series': [{
            'name': 'count of flights',
            'data': list(map(lambda row: {'name': row['destination'], 'y': row['total']}, dataset))
        }]
    }

    return JsonResponse(chart)
