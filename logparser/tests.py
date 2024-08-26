# logparser/tests.py
from django.test import TestCase
from logparser.models import LogEntry

class LogEntryTestCase(TestCase):
    def setUp(self):
        LogEntry.objects.create(
                                ip_address="127.0.0.1", 
                                date="2024-01-01T00:00:00Z", 
                                http_method="GET", 
                                uri="/test", 
                                response_code=200, 
                                response_size=123
                            )

    def test_log_entry(self):
        entry = LogEntry.objects.get(ip_address="127.0.0.1")
        self.assertEqual(entry.uri, "/test")
