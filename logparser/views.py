from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from logparser.models import LogEntry
from logparser.serializers import LogEntrySerializer


# Create your views here.
class LogEntryViewSet(viewsets.ModelViewSet):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['http_method', 'response_code']
    search_fields = ['ip_address', 'uri']
    ordering_fields = ['date', 'respons_size']