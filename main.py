from telebot import TeleBot


bot = TeleBot('7609957754:AAHWYgFo2QcyxJOuL7LCGi-J1vdFoDPyvnk')  # Ваш API токен

# Проверка никнейма
def check_nickname(nickname):
    if len(nickname) > 20:
        return "Никнейм не должен превышать 20 символов."
    if nickname[0].isdigit():
        return "Никнейм не должен начинаться с цифры."
    if not nickname.endswith("bot"):
        return "Никнейм должен заканчиваться на 'bot'."
    return "Ник одобрен!"

# Обработка команды /start с выводом выделенного жирным текста
@bot.message_handler(commands=['start'])
def start_bold(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в наш автосалон! /models, /tips, /link, /check_nickname')

# Обработка команды /models с выводом списка моделей автомобилей
@bot.message_handler(commands=['models'])
def show_models(message):
    models = "Вот некоторые популярные модели автомобилей:\n- Tesla Model S\n- BMW 3 Series\n- Audi A4\n- Mercedes-Benz C-Class"
    bot.send_message(message.chat.id, models)

# Обработка команды /tips с выводом советов по уходу за автомобилем
@bot.message_handler(commands=['tips'])
def car_tips(message):
    tips = "Советы по уходу за автомобилем:\n1. Регулярно проверяйте уровень масла.\n2. Меняйте фильтры.\n3. Следите за давлением в шинах."
    bot.send_message(message.chat.id, tips)

# Обработка команды /link с выводом ссылки на сайт о машинах
@bot.message_handler(commands=['link'])
def start_link(message):
    link = "https://www.carsguide.com.au"
    bot.send_message(message.chat.id, f'<a href="{link}">Полезная информация о машинах</a>', parse_mode='HTML')


@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == "/check_nickname":
        bot.send_message(message.chat.id, "Пожалуйста, укажите никнейм после команды.")
    else:
        result = check_nickname(message.text)
        bot.send_message(message.chat.id, result)


# Запуск бота
bot.infinity_polling()
