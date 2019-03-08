from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from metrics.filters import MetricFilter
from .models import Metric
from .serializers import MetricSerializer


class MetricList(generics.ListAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = MetricFilter
