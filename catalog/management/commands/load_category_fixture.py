from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    help = 'Добавление в таблицу category данных из фикстуры'

    def handle(self, *args, **options):
        call_command('loaddata', 'category_fixture.json')
        self.stdout.write(self.style.SUCCESS('Таблица product успешно обновлена из фикстуры'))
