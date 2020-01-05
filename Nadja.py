from Danja import match
import pickle
import telebot
from Samir2 import f as foo

admin = [542658693, 684568784]
places = []
times = []
str = ''

token = "1008644876:AAHdPfzbXGiq5WpX9IJyKVxoGnK4wYXRZ0w"
telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}
bot = telebot.TeleBot(token=token)


@bot.message_handler(commands=['start'])
def f(message):
    user = message.chat.id
    users = pickle.load(open('users.pickle', 'rb'))
    users.add(user)
    pickle.dump(users, open('users.pickle', 'wb'))
    bot.send_message(user, 'Привет участник GoTo, я Бот-Чаёк\nЯ напишу тебе когда и куда тебе придти на чаёчек ;)')


@bot.message_handler(content_types=['document'])
def f(message):
    user = message.chat.id
    if user in admin:
        try:
            if message.document.file_name.split('.')[1] == 'csv' or True:
                file_info = bot.get_file(message.document.file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                file = open('csv.csv', 'wb')
                file.write(downloaded_file)
                file.close()
                msg = bot.send_message(user, "Сохранил. А теперь мне нужны места. Вводите по одному сообщению, как закончите, напишите всё.")
                bot.register_next_step_handler(msg, place)
            else:
                bot.send_message(user, 'Отправляй мне только .CSV файлы :<')
        except Exception as e:
            bot.send_message(message, e)
    else:
        bot.send_message(user, 'Привет участник GoTo, я Бот-Чаёк\nЯ напишу тебе когда и куда тебе придти на чаёчек ;)')


@bot.message_handler(commands=['admin'])
def f(message):
    user = message.chat.id
    if user in admin:
        bot.send_message(user, '''/start - Присоединиться к рассылке GoTo,
/help - Помощь участникам,
/admin - Помощь админам,
Отправь .CSV файл, и я разобью по парам участников (/format - Правильный формат таблицы)''')
    else:
        bot.send_message(user, 'Привет участник GoTo, я Бот-Чаёк\nЯ напишу тебе когда и куда тебе придти на чаёчек ;)')


@bot.message_handler(commands=['test'])
def f(message):
    user = message.chat.id
    if user in admin or True:
        msg = bot.send_message(user, 'Это тестовая функция. Отправьте таблицу для распределения участников по комнатам. Отправьте файл csv')
        bot.register_next_step_handler(msg, super_file)
    else:
        bot.send_message(user, 'Привет участник GoTo, я Бот-Чаёк\nЯ напишу тебе когда и куда тебе придти на чаёчек ;)')


@bot.message_handler(commands=['format'])
def f(message):
    user = message.chat.id
    if user in admin:
        bot.send_message(user, '''Немножечко, как надо делать таблицу:

Первая колонка таблицы, это ФИО участника.
Затем идут колонки (домик, направление...).
Порядок важен (Первый параметр будет сильнее учитываться, чем последний)

Думаю достаточно понятно)''')
    else:
        bot.send_message(user, 'Привет участник GoTo, я Бот-Чаёк\nЯ напишу тебе когда и куда тебе придти на чаёчек ;)')


def super_file(message):
    user = message.chat.id
    try:
        if message.document.file_name.split('.')[1] == 'csv' or True:
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            file = open('Humans.csv', 'wb')
            file.write(downloaded_file)
            file.close()
            bot.send_message(user, foo())
        else:
            msg = bot.send_message(user, 'Отправляй мне только .CSV файлы :<')
            bot.register_next_step_handler(msg, super_file)
    except Exception as e:
        msg = bot.send_message(user, e)
        bot.register_next_step_handler(msg, super_file)


def place(message):
    user = message.chat.id
    txt = message.text

    if txt.lower() in ['всё', 'все']:
        msg = bot.send_message(user,
                               'Сохранил. А теперь мне нужно время. Вводите по одному сообщению, как закончите, напишите всё.')
        bot.register_next_step_handler(msg, time)
        return

    places.append(txt)
    msg = bot.send_message(user, 'Записал ;)')
    bot.register_next_step_handler(msg, place)


def time(message):
    global times
    user = message.chat.id
    txt = message.text

    if txt.lower() in ['всё', 'все']:
        pairs = match()
        if len(pairs) > len(places) * len(times):
            msg = bot.send_message(user, 'Может ещё добавите время... А то не хватает(')
            bot.register_next_step_handler(msg, time)
        else:
            for i in range(len(pairs)):
                bot.send_message(user,
                                 '{} == {}, {}, {}'.format(*pairs[i],
                                                           places[i % len(places)],
                                                           times[i // len(places)]
                                                           )
                                 )
        return

    times.append(txt)
    msg = bot.send_message(user, 'Записал ;)')
    bot.register_next_step_handler(msg, time)


bot.polling(none_stop=True, timeout=123)
