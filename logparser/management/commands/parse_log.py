# logparser/management/commands/parse_log.py
import json
import requests
from datetime import datetime
from django.core.management.base import BaseCommand
from logparser.models import LogEntry
from django.utils import timezone

class Command(BaseCommand):
    help = 'Parses an Nginx log file and stores it in the database.'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='URL of the log file')

    def handle(self, *args, **kwargs):
        url = kwargs['url']
        response = requests.get(url)

        if response.status_code != 200:
            self.stdout.write(self.style.ERROR(f'Failed to download file. Status code: {response.status_code}'))
            return
        
        content = response.text
        if not content.strip():
            self.stdout.write(self.style.ERROR('Downloaded file is empty.'))
            return

        log_lines = content.splitlines()

        for line in log_lines:
            try:
                log_entry = json.loads(line)
                time_str = log_entry['time'].split(" ")[0]
                log_date_naive = datetime.strptime(time_str, "%d/%b/%Y:%H:%M:%S")
                
                # Make the datetime timezone-aware
                log_date = timezone.make_aware(log_date_naive, timezone.utc)
                method, uri, _ = log_entry['request'].split()

                LogEntry.objects.create(
                    ip_address=log_entry['remote_ip'],
                    date=log_date,
                    http_method=method,
                    uri=uri,
                    response_code=log_entry['response'],
                    response_size=log_entry['bytes'],
                )
            except json.JSONDecodeError as e:
                self.stdout.write(self.style.ERROR(f'JSON decode error: {e}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error processing line: {line}. Exception: {e}'))

        self.stdout.write(self.style.SUCCESS('Log file parsed and stored successfully.'))
