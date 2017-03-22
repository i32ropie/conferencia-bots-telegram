import telebot

bot = telebot.TeleBot('<TOKEN>', skip_pending=True)

def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            bot.send_message(m.chat.id, m.text)
            print("[{}] {}: {}".format(m.chat.id, m.from_user.first_name, m.text))

bot.set_update_listener(listener)

bot.polling(True)
