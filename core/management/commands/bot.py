from django.core.management import BaseCommand

from bot.bot import bot_start


class Command(BaseCommand):
    help = 'Start Telegram Bot'

    def handle(self, *args, **options):
        bot_start()
