import asyncio
import logging
import os

from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

from app.secret import TELEGRAM_BOT_TOKEN

from bot.bot_ui import *
from bot.handlers.menu import hello_handler, subscribe_handler, help_handler, incorrect_handler, holidays_handler
from bot.handlers.subscribe import apply_subscribe_handler, cancel_subscribe_handler, incorrect_subscribe_input_handler, \
    remove_subscribe_handler
from bot.sender import subscribes_sender
from bot.state import BotStates


os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"


bot = Bot(token=TELEGRAM_BOT_TOKEN)
storage = MemoryStorage()
dispatcher = Dispatcher(bot=bot, storage=storage)
logging.basicConfig(level=logging.INFO)


async def on_startup(dp: Dispatcher):
    dp.register_message_handler(hello_handler, commands=[start_command], state='*')

    dp.register_message_handler(holidays_handler, regexp=holidays_button.text, state='*')
    dp.register_message_handler(holidays_handler, commands=[holidays_command], state='*')

    dp.register_message_handler(help_handler, regexp=help_button.text, state='*')
    dp.register_message_handler(help_handler, commands=[help_command], state='*')

    dp.register_message_handler(subscribe_handler, regexp=subscribe_button.text, state='*')
    dp.register_message_handler(subscribe_handler, commands=[subscribe_command], state='*')

    dp.register_message_handler(apply_subscribe_handler, regexp=time_regexp, state=BotStates.waiting_time_input)
    dp.register_message_handler(cancel_subscribe_handler, regexp=back_button.text, state=BotStates.waiting_time_input)
    dp.register_message_handler(incorrect_subscribe_input_handler, state=BotStates.waiting_time_input)

    dp.register_message_handler(remove_subscribe_handler, regexp=delete_button.text,
                                state=BotStates.waiting_subscribe_current)
    dp.register_message_handler(cancel_subscribe_handler, regexp=back_button.text,
                                state=BotStates.waiting_subscribe_current)

    dp.register_message_handler(incorrect_handler, state='*')

    await dp.bot.set_my_commands(bot_commands)

    asyncio.create_task(subscribes_sender(bot))


def bot_start():
    executor.start_polling(dispatcher, timeout=30, on_startup=on_startup)
