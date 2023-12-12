from aiogram.types import BotCommand, ReplyKeyboardMarkup, KeyboardButton

from core.models import Subscribe
from util import parser


def get_holidays_text():
    holidays = parser.get_holidays()

    if len(holidays) == 0:
        return 'Праздники сегодня отсутствуют!'

    return f'Праздники сегодня:\n' + '\n'.join(holidays)


def get_current_subscribe_text(sub: Subscribe):
    return f'Ваша текущая подписка: {sub.time.strftime("%H:%M")}\nДля удаления нажмите на соответствующую кнопку на клавиатуре'


start_command = BotCommand(command='/start', description='Запуск бота')
help_command = BotCommand(command='/help', description='Помощь')
holidays_command = BotCommand(command='/holidays', description='Просмотр праздников на сегодня')
subscribe_command = BotCommand(command='/subscribe', description='Подписка на рассылку')

holidays_button = KeyboardButton('Праздники сегодня')
subscribe_button = KeyboardButton('Подписаться на рассылку')
help_button = KeyboardButton('О боте')
back_button = KeyboardButton('Назад')
delete_button = KeyboardButton('Удалить подписку')


bot_commands = [start_command, help_command, holidays_command, subscribe_command]
bot_main_keyboard = ReplyKeyboardMarkup(keyboard=[[holidays_button], [subscribe_button], [help_button]],
                                        resize_keyboard=True)
bot_cancel_keyboard = ReplyKeyboardMarkup(keyboard=[[back_button]], resize_keyboard=True)
bot_delete_cancel_keyboard = ReplyKeyboardMarkup(keyboard=[[delete_button], [back_button]], resize_keyboard=True)


hello_message_text = 'Привет! Я праздничный бот, для взаимодействия со мной используйте команды или клавиатуру!'
subscribe_input_text = ('Чтобы получать праздники на каждый день, отправьте в чат время в формате: час:минута'
                        '\nНапример: 12:41')
incorrect_input_time_text = 'Некорректно введено время!'
apply_subscribe_text = 'Ваша подписка успешно применена!'
help_text = ('Я бот для рассылки праздников на каждый день!\nЧтобы посмотреть праздники нажмиет кнопку снизу либо '
             'введите команду /holidays\nТак же я могу присылать праздники каждый день в заданное время, чтобы '
             'подписаться, вам следует либо нажать на соответсвующую кнопку снизу, либо прописать команду /subscribe')
incorrect_text = 'Я вас не понимаю! Для помощи пропишите команду /help'
remove_subscribe_text = 'Ваша подписка успешно удалена!'


time_regexp = r'^([01]?[0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?$'
