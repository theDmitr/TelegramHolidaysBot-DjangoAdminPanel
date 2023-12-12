from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from bot.bot_ui import hello_message_text, bot_main_keyboard, bot_cancel_keyboard, subscribe_input_text, help_text, \
    incorrect_text, get_holidays_text, bot_delete_cancel_keyboard, get_current_subscribe_text

from bot.state import BotStates
from core.models import Subscribe


async def hello_handler(message: Message, state: FSMContext):
    await state.finish()
    await message.reply(hello_message_text, reply_markup=bot_main_keyboard)


async def subscribe_handler(message: Message, state: FSMContext):
    await state.finish()

    subscribes = Subscribe.objects.filter(chat_id=message.chat.id)

    if len(subscribes) == 0:
        await message.reply(subscribe_input_text, reply_markup=bot_cancel_keyboard)
        await state.set_state(BotStates.waiting_time_input)
        return

    await message.reply(get_current_subscribe_text(subscribes[0]), reply_markup=bot_delete_cancel_keyboard)
    await state.set_state(BotStates.waiting_subscribe_current)


async def help_handler(message: Message, state: FSMContext):
    await state.finish()
    await message.reply(help_text, reply_markup=bot_main_keyboard)


async def holidays_handler(message: Message, state: FSMContext):
    await state.finish()
    await message.reply(get_holidays_text(), reply_markup=bot_main_keyboard)


async def incorrect_handler(message: Message, state: FSMContext):
    await message.reply(incorrect_text, reply_markup=bot_main_keyboard)
