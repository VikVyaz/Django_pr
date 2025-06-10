from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Удаление всех данных из БД'

    def handle(self, *args, **options):
        self.clear_table(Product)
        self.clear_table(Category)

    def clear_table(self, model):
        table_name = model._meta.db_table
        answer = input(f'Очистить данные в таблице {table_name}? [y/n]:\n')
        if answer in ['', 'y', 'Y']:
            model.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f'Таблица {table_name} очищена'))
        else:
            self.stdout.write(self.style.WARNING(f'Таблица {table_name} не очищена'))
