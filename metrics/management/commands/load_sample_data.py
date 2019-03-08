import csv

from django.core.management.base import BaseCommand
from django.db import transaction

from metrics.models import Metric


class Command(BaseCommand):
    help = 'Loads sample metrics data from fixture csv file'

    def handle(self, *args, **options):
        with transaction.atomic():
            Metric.objects.all().delete()
            for row in self.load_csv():
                row['date'] = '-'.join(reversed(row['date'].split('.')))  # one line reformat dd.mm.yyyy to yyyy-mm-dd
                Metric.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Data loaded'))

    def load_csv(self):
        with open('metrics/fixtures/sample_data.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                yield row
