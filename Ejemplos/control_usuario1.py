import telebot

bot = telebot.TeleBot('<TOKEN>', skip_pending=True)

def listener(messages):
    for m in messages:
      if m.content_type == 'text':
        print("[{}] {}: {}".format(m.chat.id, m.from_user.first_name, m.text))

bot.set_update_listener(listener)

@bot.message_handler(commands=['start'])
def message_start(m):
    cid = m.chat.id
    nombre_usuario = m.from_user.first_name
    bot.send_message(cid, "¡Hola {}! Bienvenido a @{}".format(nombre_usuario, bot.get_me().username))

bot.polling(True)
