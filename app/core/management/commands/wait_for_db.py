import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""
    pass

    def handle(self, *args, **options):
        # this will run when Command is called

        self.stdout.write("Waiting for database...")

        db_connection = None
        while not db_connection:
            try:
                db_connection = connections['default']

        # django.db.connections is a dictionary-like object
        # that allows you to retrieve a specific connection using its alias.
        # 'default' is the alias of db in 'settings.py'

            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database ready."))
