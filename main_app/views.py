from django.shortcuts import render


def index(request):
    return render(request, 'main_app/start_page.html')


def train(request):
    return render(request, 'main_app/start_page.html')


def bus(request):
    return render(request, 'main_app/start_page.html')

# def filter_train(request):
#     flights_list = TrainFlight.objects.all()
#     flight_filter = FlightFilter(request.GET, queryset=flights_list)
#     return render(request, 'main_app/train.html', {'filter': flight_filter})
