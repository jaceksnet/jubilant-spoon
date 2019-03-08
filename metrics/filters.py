from django_filters import rest_framework as filters

from .models import Metric


class MetricFilter(filters.FilterSet):
    date_to = filters.DateFilter(field_name='date', lookup_expr='lte')
    date_from = filters.DateFilter(field_name='date', lookup_expr='gte')

    class Meta:
        model = Metric
        fields = ('date_to', 'date_from')
