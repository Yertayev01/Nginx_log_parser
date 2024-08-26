from django.contrib import admin
from logparser.models import LogEntry

# Register your models here,
@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'date', 'http_method', 'uri', 'response_code', 'response_size')
    list_filter = ('http_method', 'response_code')
    search_fiels = ('ip_address', 'uri')
    