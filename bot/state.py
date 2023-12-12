from aiogram.dispatcher.filters.state import StatesGroup, State


class BotStates(StatesGroup):
    waiting_time_input = State()
    waiting_subscribe_current = State()
