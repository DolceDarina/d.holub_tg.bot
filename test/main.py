import telebot
from keyboards import *
from config import token

bot = telebot.TeleBot(token)

# Состояния диалога
CHOOSE_NUM_GUESTS = 0
CHOOSE_TV = 1
CHOOSE_KETTLE = 2
CHOOSE_BATHROOM = 3
CHOOSE_BED_TYPE = 4
CHOOSE_NUM_KIDS = 5
CONFIRM_RESERVATION = 6

# Словарь для хранения данных о броне
bookings = {}

# Обработчик ввода количества гостей
@bot.message_handler(func=lambda message: True)
def handle_num_guests(message):
    chat_id = message.chat.id
    if chat_id not in bookings:
        bookings[chat_id] = {'state': CHOOSE_NUM_GUESTS}
        bot.send_message(chat_id, 'Выберите количество гостей:', reply_markup=num_guests_keyboard)
        bot.register_next_step_handler(message, handle_num_guests)
    elif bookings[chat_id]['state'] == CHOOSE_NUM_GUESTS:
        num_guests = message.text
        bookings[chat_id]['num_guests'] = num_guests
        bot.send_message(chat_id, 'Необходим телевизор в номере?', reply_markup=tv_keyboard)
        bot.register_next_step_handler(message, handle_tv)

# Обработчик выбора наличия телевизора
def handle_tv(message):
    chat_id = message.chat.id
    tv = message.text.lower() == 'да'
    bookings[chat_id]['tv'] = tv
    bot.send_message(chat_id, 'Необходим чайник в номере?', reply_markup=kettle_keyboard)
    bot.register_next_step_handler(message, handle_kettle)

# Обработчик выбора наличия чайника
def handle_kettle(message):
    chat_id = message.chat.id
    kettle = message.text.lower() == 'да'
    bookings[chat_id]['kettle'] = kettle
    bot.send_message(chat_id, 'Какое помещение вы предпочитаете: ванную или душевую кабину?', reply_markup=bathroom_keyboard)
    bot.register_next_step_handler(message, handle_bathroom)

# Обработчик выбора ванной или душевой кабины
def handle_bathroom(message):
    chat_id = message.chat.id
    bathroom = message.text
    bookings[chat_id]['bathroom'] = bathroom
    bot.send_message(chat_id, 'Какие кровати вы предпочитаете: односпальные или двуспальные?', reply_markup=bed_type_keyboard)
    bot.register_next_step_handler(message, handle_bed_type)

# Обработчик выбора типа кроватей
def handle_bed_type(message):
    chat_id = message.chat.id
    bed_type = message.text
    bookings[chat_id]['bed_type'] = bed_type
    bot.send_message(chat_id, 'Пожалуйста, проверьте детали брони:', reply_markup=confirm_keyboard)
    booking_details = get_booking_details(bookings[chat_id])
    bot.send_message(chat_id, booking_details)
    bot.register_next_step_handler(message, handle_confirm)


# Обработчик подтверждения брони
def handle_confirm(message):
    chat_id = message.chat.id
    if message.text.lower() == 'согласен':
        bot.send_message(chat_id, 'Спасибо за бронирование! Ваш номер зарезервирован.')
        # здесь можно добавить логику для сохранения брони в базе данных или отправки уведомления администратору
        del bookings[chat_id]
    else:
        bot.send_message(chat_id, 'Бронирование отменено.')
        del bookings[chat_id]

# Функция для формирования текста с деталями брони
def get_booking_details(booking):
    details = f"Количество гостей: {booking['num_guests']}\n"
    details += f"Телевизор: {'Да' if booking['tv'] else 'Нет'}\n"
    details += f"Чайник: {'Да' if booking['kettle'] else 'Нет'}\n"
    details += f"Помещение: {booking['bathroom']}\n"
    details += f"Тип кроватей: {booking['bed_type']}"
    return details

# Запуск бота
bot.polling()