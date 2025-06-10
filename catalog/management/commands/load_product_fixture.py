from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product


class Command(BaseCommand):
    help = 'Добавление в таблицу product данных из фикстуры'

    def handle(self, *args, **options):
        call_command('loaddata', 'product_fixture.json')
        self.stdout.write(self.style.SUCCESS('Таблица product успешно обновлена из фикстуры'))
