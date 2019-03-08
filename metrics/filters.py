from django.db.models import Sum, F, CharField, Value
from django_filters import rest_framework as filters

from .models import Metric

GROUP_BY_FIELDS = ('date', 'channel', 'country', 'os')
COUNTABLE_FIELDS = ('impressions', 'clicks', 'installs', 'spend', 'revenue')
ALL_FIELDS = GROUP_BY_FIELDS + COUNTABLE_FIELDS


class MetricFilter(filters.FilterSet):
    date_to = filters.DateFilter(field_name='date', lookup_expr='lte')
    date_from = filters.DateFilter(field_name='date', lookup_expr='gte')
    group_by = filters.MultipleChoiceFilter(choices=zip(GROUP_BY_FIELDS, GROUP_BY_FIELDS),
                                            method='filter_group_by')
    order_by = filters.OrderingFilter(fields=tuple(zip(ALL_FIELDS, ALL_FIELDS)))

    def filter_group_by(self, queryset, name, value):
        unused_fields = set(GROUP_BY_FIELDS) - set(value)
        unused_annotation = {field_name: Value('---', CharField()) for field_name in unused_fields}
        sums_annotation = {field_name: Sum(F(field_name)) for field_name in COUNTABLE_FIELDS}
        return queryset.values(*value).annotate(**sums_annotation).annotate(**unused_annotation)

    class Meta:
        model = Metric
        fields = ('date_to', 'date_from')
