from telebot import types

# Клавиатура для выбора количества гостей (до 5 гостей максимум)
num_guests_keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
num_guests_keyboard.add(
    types.KeyboardButton('1 гость'), types.KeyboardButton('2 гостя'), types.KeyboardButton('3 гостя'),
    types.KeyboardButton('4 гостя'), types.KeyboardButton('5 гостей')
)

# Клавиатура для выбора наличия телевизора
tv_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
tv_keyboard.add(types.KeyboardButton('Да'), types.KeyboardButton('Нет'))

# Клавиатура для выбора наличия чайника
kettle_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
kettle_keyboard.add(types.KeyboardButton('Да'), types.KeyboardButton('Нет'))

# Клавиатура для выбора типа ванной комнаты
bathroom_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
bathroom_keyboard.add(types.KeyboardButton('Ванная'), types.KeyboardButton('Душевая'))

# Клавиатура для выбора типа кровати
bed_type_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
bed_type_keyboard.add(types.KeyboardButton('Односпальная'), types.KeyboardButton('Двуспальная'))

# Клавиатура для подтверждения брони
confirm_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
confirm_keyboard.add(types.KeyboardButton('Согласен'), types.KeyboardButton('Начать заново'))