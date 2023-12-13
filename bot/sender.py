import asyncio
from datetime import timedelta

from aiogram import Bot

from bot.bot_ui import get_holidays_text
from core.models import Subscribe
from django.utils import timezone


async def subscribes_sender(bot: Bot):
    while True:
        subscribes = Subscribe.objects.get_queryset()
        current_time = timezone.now()
        current_timedelta = timedelta(hours=current_time.hour,
                                      minutes=current_time.minute,
                                      seconds=current_time.second)
        for subscribe in subscribes:
            subscribe_timedelta = timedelta(hours=subscribe.time.hour,
                                            minutes=subscribe.time.minute,
                                            seconds=subscribe.time.second)
            if current_time.date() > subscribe.last_date_check and current_timedelta > subscribe_timedelta:
                subscribe.last_date_check = current_time.date()
                subscribe.save()
                await bot.send_message(subscribe.chat_id, get_holidays_text())
        await asyncio.sleep(30)
