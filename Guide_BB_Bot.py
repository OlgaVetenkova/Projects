import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    #Телеграм позволяет автоматически уменьшить размер, для этого необходимо передать в инициализатор класса ReplyKeyboardMarkup параметру resize_keyboard значение True
    button_1 = types.KeyboardButton('О компании')
    button_2 = types.KeyboardButton('Заказ канц.товаров')
    button_3 = types.KeyboardButton('Время работы')
    button_4 = types.KeyboardButton('IT-поддержка')
    button_5 = types.KeyboardButton('Контакты сотрудников')
    button_6 = types.KeyboardButton('Зар.плата')
    button_7 = types.KeyboardButton('Где пообедать?')
    button_8 = types.KeyboardButton('Контракт')
    button_9 = types.KeyboardButton('Бронь переговорки')



    markup.add(button_1, button_2,
               button_3, button_4,
               button_5, button_6,
               button_7, button_8,
               button_9
               )

    bot.send_message(message.chat.id,
                         "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный помочь тебе разобраться как тут всё устроено.".format(
                             message.from_user, bot.get_me()),
                         parse_mode='html', reply_markup=markup)  # reply_markup - нужно чтобы вывести меню нашему пользователю (модуль для преобрахования языка html) и передаём на созданный markup

    @bot.message_handler(content_types=['text'])  #обработчик событий
    def bot_message(message):
        if message.chat.type == 'private':   # private - значит является личным сообщением, а не, например, телеграм-каналом
            if message.text == 'О компании':
                bot.send_message(message.chat.id, 'Информацию о Компании можешь посмотреть здесь: https://bbrovar.by/ru/about-us/')  #message.chat.id – идентификатор чата
            elif message.text == 'Заказ канц.товаров':
                bot.send_message(message.chat.id, 'Подойди на ресепшн. Наш офис-менеджер Виктория даст тебе всё необходимое для работы.')
            elif message.text == 'Время работы':
                bot.send_message(message.chat.id, 'Время работы: пн-пт, 9-00 - 18-00. Обед: 13.00 - 14.00')
            elif message.text == 'IT-поддержка':
                bot.send_message(message.chat.id, 'E-mail службы IT-поддержки: support@bbrovar.by')
            elif message.text == 'Контакты сотрудников':
                bot.send_message(message.chat.id, 'Здесь ссылка на контактную информацию сотрудников компании 'f'{config.CONTACTS_LIST}')
            elif message.text == 'Зар.плата':
                bot.send_message(message.chat.id, 'Заработная плата начисляется на карту двумя частями: 7 и 19 числа для сотрудников Бобруйского бровара, 6 и 18 числа для сотрудников Оазис Груп.')
            elif message.text == 'Где пообедать?':
                bot.send_message(message.chat.id, 'В соседнем здании "Белтаможсервис" есть отличная столовая ;) Также на 1-м этаже нашего офиса находится 2 буфета, где можно перекусить.')
            elif message.text == 'Контракт':
                bot.send_message(message.chat.id, 'Твой контракт будет передан отделом кадров (г.Бобруйск) в Минск ориентировочно через 2 недели со дня написания заявления о трудоустройстве.')
            elif message.text == 'Бронь переговорки':
                bot.send_message(message.chat.id, 'Для брони комнаты переговоров пройди по ссылке: 'f'{config.MEETING_ROOM}')
            elif message.text.lower() == 'привет':
                #bot.send_message(message.chat.id, 'Привет :) нажми на кнопку меню справа в строке ввода сообщений.')
                bot.send_video(message.chat.id, 'https://i.gifer.com/DSt1.gif', None, 'Хэй! Привет :) нажми на кнопку меню справа в строке ввода сообщений.')
            else:
                bot.send_message(message.chat.id, ':) Давай попробуем ещё раз - нажми на кнопку меню справа в строке ввода сообщений.')


bot.polling(none_stop=True)  #чтобы бот не отключался


# Добавить кнопки/ если упоминается какое-то слово if x in message/ разные виды приветствий/ добавить бобра + стикеры (возможно свои)

# Декоратор @message_handler реагирует на входящие сообщение.
# Message – это объект из Bot API, содержащий в себе информацию о сообщении. Полезные поля:
# message.chat.id – идентификатор чата
# message.from.id – идентификатор пользователя
# message.text – текст сообщения
# Функция send_message принимает идентификатор чата (берем его из сообщения) и текст для отправки.