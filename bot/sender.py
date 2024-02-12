import asyncio

from aiogram import Bot

from bot.bot_ui import get_holidays_text
from core.models import Subscribe
from django.utils import timezone


async def subscribes_sender(bot: Bot):
    while True:
        subscribes = Subscribe.objects.get_queryset()
        current_time = timezone.now()
        print(current_time)
        for subscribe in subscribes:
            if (current_time.date() > subscribe.last_date_check and
                    current_time.hour == subscribe.time.hour and
                    current_time.minute == subscribe.time.minute):
                subscribe.last_date_check = current_time.date()
                subscribe.save()
                await bot.send_message(subscribe.chat_id, get_holidays_text())
        await asyncio.sleep(30)
