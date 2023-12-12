from datetime import datetime, timedelta

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from bot.bot_ui import bot_main_keyboard, incorrect_input_time_text, apply_subscribe_text, help_text, \
    remove_subscribe_text
from core.models import Subscribe

from django.utils import timezone


async def remove_subscribe_handler(message: Message, state: FSMContext):
    Subscribe.objects.filter(chat_id=message.chat.id).first().delete()
    await message.reply(remove_subscribe_text, reply_markup=bot_main_keyboard)
    await state.finish()


async def apply_subscribe_handler(message: Message, state: FSMContext):
    Subscribe.objects.create(
        chat_id=message.chat.id,
        time=datetime.strptime(message.text, '%H:%M'),
        last_date_check=(timezone.now() - timedelta(days=1)).date()
    )
    await message.reply(apply_subscribe_text, reply_markup=bot_main_keyboard)
    await state.finish()


async def cancel_subscribe_handler(message: Message, state: FSMContext):
    await message.reply(help_text, reply_markup=bot_main_keyboard)
    await state.finish()


async def incorrect_subscribe_input_handler(message: Message, state: FSMContext):
    await message.reply(incorrect_input_time_text)
