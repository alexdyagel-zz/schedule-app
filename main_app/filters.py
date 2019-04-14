import django_filters

from main_app.models import BusFlight, TrainFlight


class BusFilter(django_filters.FilterSet):
    departure_railway = django_filters.CharFilter(lookup_expr='icontains')
    destination_railway = django_filters.CharFilter(lookup_expr='icontains')
    departure_date_gt = django_filters.DateFilter(field_name='departure_date', lookup_expr='gt')
    departure_date_lt = django_filters.DateFilter(field_name='departure_date', lookup_expr='lt')
    departure_time_gt = django_filters.TimeFilter(field_name='departure_time', lookup_expr='gt')
    departure_time_lt = django_filters.TimeFilter(field_name='departure_time', lookup_expr='lt')

    class Meta:
        model = BusFlight
        fields = ['departure_railway', 'destination_railway', 'departure_date_gt', 'departure_date_lt',
                  'departure_time_gt', 'departure_time_lt']


class TrainFilter(django_filters.FilterSet):
    departure_railway = django_filters.CharFilter(lookup_expr='icontains')
    destination_railway = django_filters.CharFilter(lookup_expr='icontains')
    departure_date_gt = django_filters.DateFilter(field_name='departure_date', lookup_expr='gt')
    departure_date_lt = django_filters.DateFilter(field_name='departure_date', lookup_expr='lt')
    departure_time_gt = django_filters.TimeFilter(field_name='departure_time', lookup_expr='gt')
    departure_time_lt = django_filters.TimeFilter(field_name='departure_time', lookup_expr='lt')

    class Meta:
        model = TrainFlight
        fields = ['departure_railway', 'destination_railway', 'departure_date_gt', 'departure_date_lt',
                  'departure_time_gt', 'departure_time_lt']
